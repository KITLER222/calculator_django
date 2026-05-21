from django.db import models


class CalculatorSession(models.Model):
    session_key = models.CharField(max_length=100)

    def str(self):
        return self.session_key


class Example(models.Model):
    text = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    session = models.ForeignKey(
        CalculatorSession,
        on_delete=models.CASCADE
    )

    def str(self):
        return self.text + " = " + self.result