from django.shortcuts import render, redirect

dropdown_nav_links_data = {
        'article_categories': ['Exercises', 'Programmes', 'Nutrition', 'Supplements', 'Training', 'Science',
                               'Interviews', 'Equipment'],
        'exercise_bodyparts': ['Legs', 'Shoulders', 'Arms', 'Back', 'Chest', 'Core', 'Full Body']
    }


def index_register_view(request):
    if request.user.pk:
        return redirect('articles list')
    return render(request, 'account/index-sign-up.html')
