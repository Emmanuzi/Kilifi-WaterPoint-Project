# AGENTS.md

## Summary
Django MVP for water point mapping and fault reporting in Kilifi County. Scope is defined in `PRD.md`. Section 5 (Out of Scope) is off limits.

## Stack
- Django and Django REST Framework
- MySQL 8
- Django Templates with plain HTML, CSS and JavaScript
- Leaflet.js
- Africa's Talking
No React, Node.js, Celery or extra packages.

## Conventions
- Apps live in `apps/` with `AppConfig.name = "apps.<name>"`.
- Views stay thin. Business rules go in `services.py`.
- Report status changes only through `reports/services.py`.
- Pages use Django Templates. JSON uses DRF.
- Settings come from the environment; never hard-code secrets.
- Phone numbers are visible to staff only.

## Commands
- `python manage.py runserver`
- `python manage.py test`
- `python manage.py makemigrations`
- `python manage.py migrate`

## Workflow
- Make small, focused changes.
- Ask before adding a dependency.
