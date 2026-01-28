@echo off

call mamba install -c conda-forge ^
    django ^
    django-jinja ^
    django-session-security ^
    django-guardian ^
    django-crispy-forms ^
    crispy-bootstrap5 ^
    numpy ^
    pandas ^
    pydicom ^
    pillow ^
    opencv ^
    matplotlib ^
    simpleitk

@rem Installing dependencies using pip
@rem pip install django django-jinja django-session-security django-guardian django-crispy-forms crispy-bootstrap5 numpy pandas pydicom pillow opencv matplotlib simpleitk