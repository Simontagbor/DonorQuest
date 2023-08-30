from django.db import models

class DonationTarget(models.Model):
    """Represents a donation target set by a user."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Target for {self.user_profile.profile_name}"

    class Meta:
        verbose_name_plural = "Donation Targets"

