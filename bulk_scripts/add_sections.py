from evaluations.models import Section

# EXAMPLE Section(section_name='Display', section_order=6),
def bulk_add_sections():
    Section.objects.bulk_create([
        Section(section_name='Analytics', section_order=9),
        Section(section_name='Terms', section_order=8),
        ])
    
