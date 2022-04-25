from django.db import models


class Base(models.Model):
    """Following fields are abstract and will be use in All over the project Any time Anywhere"""
    create_by = models.BigIntegerField(db_column='CreatedBy', null=True, blank=True, default=0)
    create_on = models.DateTimeField(db_column='CreatedOn', auto_now_add=True)
    modified_by = models.BigIntegerField(db_column='ModifiedBy', null=True, blank=True, default=0)
    modified_on = models.DateTimeField(db_column='ModifiedOn', auto_now=True)
    deleted_by = models.BigIntegerField(db_column='DeletedBy', null=True, blank=True, default=0)
    deleted_on = models.DateTimeField(db_column='DeletedOn', auto_now=True)
    status = models.BigIntegerField(db_column='Status', default=0, help_text='I will use this field for making'
                                                                             'the status like pending approved and '
                                                                             'for some other purpose by Default it is '
                                                                             'Zero which has no meaning', )

    class Meta:
        abstract: True



