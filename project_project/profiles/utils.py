from project_project.accounts.models import AppUser
from project_project.profiles.models import Contract
from project_project.sport_app.models import Goal


def check_for_active_contract(trainee, coach):
    have_active_contract = Contract.objects.filter(client=trainee, coach=coach, is_active=True)
    if have_active_contract:
        return True
    return False


def get_times_hired_coach(coach):
    return len(Contract.objects.filter(coach=coach))


def get_num_active_contracts_coach(coach):
    return len(Contract.objects.filter(coach=coach, is_active=True))


def get_active_trainees(coach):
    return [contract.client for contract in Contract.objects.filter(coach=coach, is_active=True)]


def get_goals_active_trainees(coach):
    active_trainees = get_active_trainees(coach)
    trainee_goals = {}
    if active_trainees:
        for trainee in active_trainees:
            goals = trainee.traineeprofile.get_goals()
            trainee_goals[trainee] = goals
    return trainee_goals

