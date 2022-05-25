from django.db import models


# Create your models here.

class Champion(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}".format(self.id, self.name)


class Path(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(default="description")
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}".format(self.id, self.name)


class Keystone(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}".format(self.id, self.name)


class Alternative_Keystone(models.Model):
    alternative_keystone =  models.ForeignKey(Keystone, null=True, blank=True, on_delete=models.CASCADE)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{0}".format(self.alternative_keystone)



class Slot_Rune_One(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)


class Slot_Rune_Two(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)


class Slot_Rune_Three(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)


class Slot_Shard_One(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)


class Slot_Shard_Two(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)


class Slot_Shard_Three(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    #Show data when we wanna print an object
    
    
    def __str__(self):
        return "{1}({0})".format(self.id, self.name)

class Item(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    
    
    def __str__(self):
        return "{0}".format(self.name)


class Skill_Max(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    
    
    def __str__(self):
        return "{0}".format(self.name)


class Difficulty(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    
    
    def __str__(self):
        return "{0}".format(self.name)


class Rune(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    path = models.ForeignKey(Path, null=False, blank=False, on_delete=models.CASCADE)
    keystone = models.ForeignKey(Keystone, null=False, blank=False, on_delete=models.CASCADE)
    slot_rune_one = models.ForeignKey(Slot_Rune_One, null=False, blank=False, on_delete=models.CASCADE)
    slot_rune_two = models.ForeignKey(Slot_Rune_Two, null=False, blank=False, on_delete=models.CASCADE)
    slot_rune_three = models.ForeignKey(Slot_Rune_Three, null=False, blank=False, on_delete=models.CASCADE)
    slot_shard_one = models.ForeignKey(Slot_Shard_One, null=False, blank=False, on_delete=models.CASCADE)
    slot_shard_two = models.ForeignKey(Slot_Shard_Two, null=False, blank=False, on_delete=models.CASCADE)
    slot_shard_three = models.ForeignKey(Slot_Shard_Three, null=False, blank=False, on_delete=models.CASCADE)
    notes = models.TextField(null=False, blank=True)


class Matchup(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    champions = models.ForeignKey(Champion, null=False, blank=False, on_delete=models.CASCADE)
    rune = models.ForeignKey(Keystone, null=True, blank=True, on_delete=models.CASCADE)
    slot_rune_one = models.ForeignKey(Slot_Rune_One, null=True, blank=True, on_delete=models.CASCADE)
    slot_rune_two = models.ForeignKey(Slot_Rune_Two, null=True, blank=True, on_delete=models.CASCADE)
    slot_rune_three = models.ForeignKey(Slot_Rune_Three, null=True, blank=True, on_delete=models.CASCADE)
    alternative_keystone =  models.ForeignKey(Alternative_Keystone, null=True, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    skill_max = models.ForeignKey(Skill_Max, null=False, blank=False, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, null=False, blank=False, on_delete=models.CASCADE)
    comments =  models.TextField()
    notes = models.TextField(null=False, blank=True)


    def __str__(self):
        return "{0}{1}".format(self.champions, self.id)


class Update(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    date = models.DateField()
    comments =  models.CharField(max_length=1000)


    def __str__(self):
        return "{0}".format(self.date)