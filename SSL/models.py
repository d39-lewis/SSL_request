from django.db import models


class SSLRequest(models.Model):
    # Basic fields for SSL request
    domain = models.CharField(max_length=1000, help_text="The domain name for the SSL request.")
    country = models.CharField(max_length=3, help_text="Country code (ISO format).")
    state = models.CharField(max_length=300, help_text="State or province name.")
    locality = models.CharField(max_length=300, help_text="City or locality.")
    organisation = models.CharField(max_length=300, help_text="Name of the organization.")

    # JSON field for SAN (Subject Alternative Names) list
    san_list = models.JSONField(blank=True, null=True, help_text="List of alternative domain names (SANs).")

    # Key generation decision and details
    key_decision = models.CharField(
        max_length=3,
        choices=[("yes", "Yes"), ("no", "No")],
        help_text="Indicates whether a key needs to be generated.",
    )
    key_yes_size = models.IntegerField(
        blank=True, null=True, default=2048,
        help_text="Key size in bits (only applicable if key is being generated).",
    )
    key_yes_password = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Password for the key (optional).",
    )
    key_yes_name = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="File name for the generated key.",
    )
    key_no_name = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="File name for the existing key (if not generating a new key).",
    )

    # Optional: Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the request was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the request was last updated.")

    def __str__(self):
        return self.domain



