from django.db import models

DONATION_CHOICES = [
    ('full', 'تبرع بكامل الأضحية'),
    ('half', 'استلام نصفها'),
]

STATUS_CHOICES = [
    ('paid', 'تم الدفع'),
    ('booked', 'تم حجز الأضحية'),
    ('slaughtered', 'تم الذبح'),
    ('cutting', 'تم التقطيع'),
    ('half_ready', 'جاهز للاستلام'),
    ('distributing', 'جاري التوزيع'),
    ('done', 'تم التوزيع'),
]


class Udhiyah(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    donation_type = models.CharField(max_length=10, choices=DONATION_CHOICES, default='full')  # ✅ moved inside
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
