from django.db import models


class Locode(models.Model):
    locode = models.CharField(max_length=2)
    name = models.CharField(max_length=256)
    name_wo = models.CharField(max_length=256)
    sub_div = models.CharField(max_length=3)
    func = models.CharField(max_length=8)
    status = models.CharField(max_length=2)
    date = models.CharField(max_length=32)
    iata = models.CharField(max_length=256)
    coordinates = models.CharField(max_length=64)
    remarks = models.CharField(max_length=256)

    @classmethod
    def create_from_csv(cls, csv_string, save=False):
        data = csv_string.split(',')[1:]
        data.pop(4)    # remove extra unspecified column
        fileds = [
            'locode', 'name', 'name_wo', 'sub_div', 'func', 'status',
            'date', 'iata', 'coordinates', 'remarks',
        ]

        obj = cls()
        for i, field in enumerate(fileds):
            setattr(obj, field, data[i].strip('"'))

        if save:
            obj.save()
        return obj
