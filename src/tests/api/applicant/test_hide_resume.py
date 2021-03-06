import pytest
from django.forms import model_to_dict
from django.utils import timezone

from hr import factories
from hr import models

pytestmark = [
    pytest.mark.django_db(transaction=True)
]


def test_ok(jsonrpc_request, freezer, user):
    resume = factories.ResumeFactory.create(
        user=user,
        published=True,
    )
    assert resume.state == models.ResumeState.PUBLISHED
    assert resume.published_at == timezone.now()

    resp = jsonrpc_request(
        'hide_resume',
        {
            'id': resume.id,
        },
    )

    assert resp.get('result') == {
        'id': resume.id,
        'state': 'HIDDEN',
        'current_position': resume.current_position,
        'desired_position': resume.desired_position,
        'skills': [],
        'experience': resume.experience,
        'bio': resume.bio,
        'created_at': resume.created_at.isoformat(),
        'published_at': None,
    }, resp.get('error')

    resume.refresh_from_db()
    assert resume.state == models.ResumeState.HIDDEN
    assert resume.published_at is None


def test_not_published__wrong_state(jsonrpc_request, user):
    resume = factories.ResumeFactory.create(user=user)
    assert resume.state == models.ResumeState.DRAFT

    resp = jsonrpc_request(
        'hide_resume',
        {
            'id': resume.id,
        },
    )

    assert resp.get('error') == {'code': 3002, 'message': 'Resume has not allowed state for this method'}

    old_resume = model_to_dict(resume)

    resume.refresh_from_db()
    actual_resume = model_to_dict(resume)
    assert old_resume == actual_resume


def test_other_user_resume__not_found(jsonrpc_request, user):
    resume = factories.ResumeFactory.create(published=True)
    assert resume.user_id != user.id

    resp = jsonrpc_request(
        'hide_resume',
        {
            'id': resume.id,
        },
    )

    assert resp.get('error') == {'code': 3001, 'message': 'Resume not found'}

    old_resume = model_to_dict(resume)

    resume.refresh_from_db()
    actual_resume = model_to_dict(resume)
    assert old_resume == actual_resume


def test_resume_does_not_exist__not_found(jsonrpc_request):
    assert models.Resume.objects.count() == 0

    resp = jsonrpc_request(
        'hide_resume',
        {
            'id': 1,
        },
    )

    assert resp.get('error') == {'code': 3001, 'message': 'Resume not found'}
