
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
#from slughifi import slughifi



	

class Ano(models.Model):
	ano = models.CharField(max_length=60)
	slug_ano = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.ano

	def save(self, *args, **kwargs):
		if not self.slug_ano:
			self.slug_ano = slugify(self.ano)
		super(Ano, self).save(*args, **kwargs)

class Sector(models.Model):
	sector = models.CharField(max_length=60)
	

	slug_sector = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.sector

	def save(self, *args, **kwargs):
		if not self.slug_sector:
			self.slug_sector = slugify(self.sector)
		super(Sector, self).save(*args, **kwargs)

class Unidad(models.Model):
	unidad = models.CharField(max_length=60)
	codigo = models.CharField(max_length=60)
	sector = models.ForeignKey(Sector)
	slug_unidad = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.unidad

	def save(self, *args, **kwargs):
		if not self.slug_unidad:
			self.slug_unidad = slugify(self.unidad)
		super(Unidad, self).save(*args, **kwargs)

class Prog(models.Model):
	prog = models.CharField(max_length=60)
	slug_prog = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.prog

	def save(self, *args, **kwargs):
		if not self.slug_prog:
			self.slug_prog = slugify(self.prog)
		super(Prog, self).save(*args, **kwargs)

class SubP(models.Model):
	subp = models.CharField(max_length=60)
	slug_subp = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.subp

	def save(self, *args, **kwargs):
		if not self.slug_subp:
			self.slug_subp = slugify(self.subp)
		super(Subp, self).save(*args, **kwargs)

class Proy(models.Model):
	proy = models.CharField(max_length=60)
	slug_proy = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.proy

	def save(self, *args, **kwargs):
		if not self.slug_proy:
			self.slug_proy = slugify(self.proy)
		super(Proy, self).save(*args, **kwargs)

class SubP2(models.Model):
	subp2 = models.CharField(max_length=60)
	slug_subp2 = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.subp2

	def save(self, *args, **kwargs):
		if not self.slug_subp2:
			self.slug_subp2 = slugify(self.subp2)
		super(SubP2, self).save(*args, **kwargs)

class Rec(models.Model):
	rec = models.CharField(max_length=60)
	slug_rec = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.rec

	def save(self, *args, **kwargs):
		if not self.slug_rec:
			self.slug_rec = slugify(self.rec)
		super(Rec, self).save(*args, **kwargs)



class Sit(models.Model):
	sit = models.CharField(max_length=60)
	slug_sit = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.sit

	def save(self, *args, **kwargs):
		if not self.slug_sit:
			self.slug_sit = slugify(self.sit)
		super(Sit, self).save(*args, **kwargs)





class Fuente(models.Model):
	fuente = models.CharField(max_length=60)
	slug_fuente = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.fuente

	def save(self, *args, **kwargs):
		if not self.slug_fuente:
			self.slug_fuente = slugify(self.fuente)
		super(Fuente, self).save(*args, **kwargs)

class Proyecto(models.Model):

	nombre = models.CharField(max_length=140)
	ano = models.ForeignKey(Ano)
	prog = models.ForeignKey(Prog)
	subp = models.ForeignKey(SubP)
	proy = models.ForeignKey(Proy)
	subp2 = models.ForeignKey(SubP2)
	rec = models.ForeignKey(Rec)
	sit = models.ForeignKey(Sit)
	fuente = models.ForeignKey(Fuente)
	unidad = models.ForeignKey(Unidad)
	sector = models.ForeignKey(Sector)
	a_inicial = models.CharField(max_length=60)
	a_vigente = models.CharField(max_length=60)
	compromisos = models.CharField(max_length=140)
	pagos = models.CharField(max_length=60)
	slug_proyecto = models.SlugField(max_length=250, blank=True, default='')

	
	
	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug_proyecto:
			self.slug_proyecto = slugify(self.nombre)
		super(Proyecto, self).save(*args, **kwargs)