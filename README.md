# Evenza - Event Management Platform

Evenza is a seamless, all-in-one Event Management Platform designed to transform dreams into reality. With a scalable and beautifully designed interface, Evenza empowers organizers, service providers, and attendees to connect effortlessly.

## Features

### User Roles
- **Admin**: System management and oversight
- **Users**: Event planning and booking
- **Service Providers**: Offer event-related services
- **Organizations**: Manage events and services

### Key Functionalities
- User authentication and profile management
- Package booking system
- Service provider showcase and ratings
- Complaint and feedback system
- Payment processing
- Work portfolio gallery
- Real-time messaging system

## Technical Stack

- **Backend**: Django 5.1.4
- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Bootstrap
  - jQuery
- **Database**: Django ORM
- **Additional Libraries**:
  - Font Awesome 5.15.4
  - Google Fonts
  - Chart.js

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Create and activate a virtual environment:
```bash
python -m venv MainEnv
source MainEnv/bin/activate  # On Windows: MainEnv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Configure the database:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
EMP/
├── Admin/
├── Guest/
├── Organization/
├── Serviceprovider/
├── User/
├── static/
│   ├── Admin/
│   └── Main/
└── templates/
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project uses templates from HTML Codex under their standard license. For more information, visit: https://htmlcodex.com/license

## Security Notes

For production deployment:
- Change the Django secret key
- Set DEBUG = False
- Configure proper ALLOWED_HOSTS
- Implement proper security measures