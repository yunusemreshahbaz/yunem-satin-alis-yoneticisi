from django.db import models

class SatinAlim(models.Model):
    tedarikci = models.CharField(max_length=255)
    urun_adi = models.CharField(max_length=255)
    birim_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    kdv_orani = models.DecimalField(max_digits=5, decimal_places=2)
    
    # KDV'li fiyat hesaplanabilir, ama isteğe bağlı ayrı da tutulabilir
    @property
    def kdvli_fiyat(self):
        return self.birim_fiyat * (1 + self.kdv_orani / 100)

    def __str__(self):
        return f"{self.urun_adi} - {self.tedarikci}"
