from django.db import models

STATUS_CHOICES = [
    ('paid', 'تم الدفع'),
    ('booked', 'تم حجز الأضحية'),
    ('slaughtered', 'تم الذبح'),
    ('cutting', 'تم التقطيع'),
    ('distributing', 'جاري التوزيع'),
    ('done', 'تم التوزيع'),
]

class Udhiyah(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.status})"
