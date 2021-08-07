from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


def upload_attatchment_to(instance, filename):
    return 'banners/{filename}'.format(filename=filename)

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=500, unique=True)
  author = models.CharField(max_length=225, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  banner = models.FileField(_("Image"), upload_to=upload_attatchment_to, default="")

  def __str__(self):
      return self.title


class BlogSummary(models.Model):
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False)

  def __str__(self) -> str:
      return self.blog.title


class BlogSection(models.Model):
  sub_title = models.CharField(max_length=500, blank=False)
  blog = models.ForeignKey(Blog, on_delete=CASCADE, blank=False)

  def __str__(self) -> str:
      return f'{self.blog.title} - {self.sub_title}'


class SummaryParagraph(models.Model):
  details = models.TextField()
  summary = models.ForeignKey(BlogSummary, on_delete=CASCADE, blank=False)

  def __str__(self) -> str:
      return f'{self.summary.blog.title} - Subtitle ({self.id})'


class SectionParagraph(models.Model):
  details = models.TextField()
  section = models.ForeignKey(BlogSection, on_delete=CASCADE)

  def __str__(self) -> str:
      return f'{self.section.sub_title} - {self.id}'
