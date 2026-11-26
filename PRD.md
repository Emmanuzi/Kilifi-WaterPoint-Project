# Kilifi WaterPoint: Product Requirements (MVP)

**Version:** 0.2 draft | **Updated:** 26 November 2026 | **Type:** Academic prototype, team of 4

## 1. Problem Statement

- Water points in Kilifi County break down, and residents have no way to report a fault or check whether a water point works before walking to it.
- Staff have no structured way to verify, assign and track repairs, so fixes are slow and invisible.
- Residents get little warning of planned shortages, and no verified dataset of the county's water points exists.
- **MVP goal:** in one pilot ward, a fault goes from report to verified repair with visible status.

## 2. Target Users

- **Resident** (no account): browses the map, finds nearby water points, reports and tracks faults, mostly on a phone with limited data. Identified by phone number.
- **Technician** (login): sees assigned jobs, updates progress, records repair notes.
- **Administrator** (login): manages water points, verifies reports, assigns technicians, publishes shortage advisories.
- **Pilot area:** one ward in Kilifi County (to be confirmed).

## 3. Core MVP Features

### Must have

1. **Roles and login.** Administrator and technician accounts using Django auth. Users and wards are managed through the Django admin.
2. **Water point map.** Leaflet on OpenStreetMap tiles, with points colour-coded working or faulty. Status updates as linked reports are verified and resolved.
3. **Nearby search.** A "near me" button lists the closest water points using MySQL `ST_Distance_Sphere`.
4. **Fault reporting.** Water point, category (no water, broken pump, contaminated, other), description, optional photo and phone number. Returns a report reference.
5. **Report tracking.** Reference plus phone number shows the current status and history.
6. **Administrator queue.** Filter by status, verify or reject (with a reason), assign a technician, update status, add and edit water points.
7. **Technician jobs.** "My jobs" with location, description and photo. Start work, or resolve with a note.
8. **Report workflow.** Reported → Verified → Assigned → In Progress → Resolved → Closed, or Rejected. The administrator closes after resolution. Only valid transitions are allowed, each logged with user and time.
9. **Shortage advisories.** The administrator publishes an advisory for a ward (message and date), shown on the home page.

### Should have (if time allows)

10. **Outbound SMS** through the Africa's Talking sandbox: report received, status changes, and advisory broadcast to numbers that reported in that ward.

**Done when** a resident reports a fault, an administrator verifies and assigns it, a technician resolves it, and the resident sees each status change, on sample pilot-ward data.

**Core entities:** Ward, User (role), WaterPoint, Report, ReportUpdate, Assignment, Advisory. The ERD in `docs/diagrams/` has the final fields.

### Non-functional requirements

- **Mobile-first and light:** works on small screens and slow connections, with no heavy JavaScript frameworks.
- **Security and privacy:** CSRF protection, role checks on every staff page and endpoint, image-only uploads with a size limit, and phone numbers visible to staff only.
- **Validation and testing:** Kenyan phone number format, valid coordinates, and automated tests for status transitions and the proximity query.
- **Delivery:** runs locally from the README steps. Deployment is not required.

## 4. Tech Stack

- **Backend:** Django and Django REST Framework. Business rules live in service functions, not views. DRF serves the JSON for the map and report form.
- **Database:** MySQL 8.0+ with stored coordinates for spatial queries.
- **Frontend:** Django Templates, HTML5, CSS and vanilla JavaScript.
- **Mapping:** Leaflet.js with OpenStreetMap tiles (keep the attribution).
- **SMS:** Africa's Talking API, sandbox only (should-have).
- **Tooling:** Git and GitHub (branches and pull requests). OpenCode with AI agents assists, and teammates review every change before merging.
- **Constraints:** no React, Node.js, Celery or other extra frameworks. Secrets stay in `.env`, never in the repository.

## 5. Out of Scope for MVP

- Inbound SMS and USSD reporting.
- Resident registration and accounts.
- Any area beyond the pilot ward, or a full county dataset.
- Duplicate-report detection, crowd verification, and a "returned to administrator" job state.
- Analytics and resolution-time dashboards.
- Swahili or other language versions, a native mobile app, offline mode and real-time push updates.
- Background job queues, large-scale bulk SMS, and integration with utility, WASREB or county systems.
- Advanced geospatial features such as polygons and routing.
- Production hardening: deployment, monitoring, load testing and security audit.

## 6. Open Questions

- Which ward is the pilot, and who collects its water point data?
- What is the deadline, and what must the demo show (live SMS or sandbox)?
