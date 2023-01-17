from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
User = get_user_model()


def test_login_user(client, faker):
    url = reverse('login')
    email = faker.email()
    password = faker.password()
    phone = faker.phone_number()
    user = User.objects.create(
        email=email,
        first_name=email,
        phone=phone,
        is_phone_valid=True
    )
    user.set_password(password)
    user.save()
    # get login page
    response = client.get(url)
    assert response.status_code == 200

    data = {
        'password': faker.password()
    }
    # post data login form
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors['__all__'][0] == 'Email ot phone number is required'

    data['username'] = faker.email()
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context['form'].errors['__all__'][0] == 'Please enter a correct email address and password. Note that both fields may be case-sensitive.'

    data['username'] = email
    data['password'] = password
    response = client.post(url, data=data)
    assert response.status_code == 302
