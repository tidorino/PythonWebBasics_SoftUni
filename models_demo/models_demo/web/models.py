from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=40
    )

    age = models.IntegerField()

    email = models.EmailField(
        'EMAIL',  # verbose_name = 'EMAIL'
        unique=True,
        max_length=200,

    )

    works_full_time = models.BooleanField(
        default=True,
        blank=True,
        null=True,
    )
    my_level = models.CharField(
        max_length=3,
        choices=(
            ('jr', ' junior'),
            ('reg', 'regular'),
            ('sr', 'senior'),
        ),
        null=True,
    )
    job_level = models.CharField(
        max_length=30,
        default='junior',
    )

    business_account = models.CharField(
        max_length=30,
        unique=True,
        default='unknown',
    )

    second_email_address = models.EmailField(blank=True)
    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        default=1
    )

    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'
