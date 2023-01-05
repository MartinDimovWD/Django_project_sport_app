from project_project.accounts.models import AppUser
from project_project.profiles.models import Contract


def check_for_active_contract(trainee, coach):
    have_active_contract = Contract.objects.filter(client=trainee, coach=coach, is_active=True)
    if have_active_contract:
        return True
    return False
