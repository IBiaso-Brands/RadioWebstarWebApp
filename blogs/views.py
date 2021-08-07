from django.shortcuts import render
from .models import Blog, BlogSection, BlogSummary, SummaryParagraph, SectionParagraph

# Create your views here.
def index(request):
  
  blogs = []
  allBlogs = Blog.objects.all()
  
  if allBlogs.count != 0 :
    for blog in allBlogs:
      blogs.append({
        'blog': blog,
        'summaries': SummaryParagraph.objects.filter(summary=BlogSummary.objects.filter(blog=blog).first()),
        'sections': BlogSection.objects.filter(blog=blog)
      })

  print(blogs)

  return render(request, 'index.html', {'blogs': blogs})
