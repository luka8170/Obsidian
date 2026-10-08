#!/usr/bin/env python3
"""
HTML to Word Document Converter for SANG JIN HAN Resume
This script converts the HTML resume to a professionally formatted Word document
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.shared import OxmlElement, qn
import os

def add_hyperlink(paragraph, text, url):
    """Add a hyperlink to a paragraph"""
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    
    # Color
    c = OxmlElement('w:color')
    c.set(qn('w:val'), "0000FF")
    rPr.append(c)
    
    # Underline
    u = OxmlElement('w:u')
    u.set(qn('w:val'), "single")
    rPr.append(u)
    
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    
    paragraph._p.append(hyperlink)
    return hyperlink

def create_resume_document():
    """Create the Word document for the resume"""
    doc = Document()
    
    # Set document margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
    
    # Header Section
    header = doc.add_heading('SANG JIN HAN', level=1)
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header.runs[0]
    header_run.font.size = Pt(24)
    header_run.font.color.rgb = RGBColor(30, 60, 114)  # #1e3c72
    
    # Subtitle
    subtitle = doc.add_paragraph('Resume for WR Group Korea Branch Manager Position')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle_run = subtitle.runs[0]
    subtitle_run.font.size = Pt(14)
    subtitle_run.font.color.rgb = RGBColor(42, 82, 152)  # #2a5298
    subtitle_run.bold = True
    
    # Date
    date_para = doc.add_paragraph('September 2, 2025')
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_run = date_para.runs[0]
    date_run.font.size = Pt(12)
    date_run.italic = True
    
    # Add a line break
    doc.add_paragraph()
    
    # Personal Information Section
    doc.add_heading('PERSONAL INFORMATION', level=2)
    
    personal_info = [
        ('Name:', 'Sang Jin Han'),
        ('Date of Birth:', 'May 28, 1973 (Age 52)'),
        ('Contact:', '+82-10-4167-0528'),
        ('Email:', 'frankston@naver.com'),
        ('Address:', 'Bundang-gu, Seongnam-si, Gyeonggi-do, South Korea'),
        ('Military Service:', 'Korean Army, Sergeant (Jan 1995 - Mar 1997)')
    ]
    
    for label, value in personal_info:
        para = doc.add_paragraph()
        run1 = para.add_run(label)
        run1.bold = True
        run1.font.color.rgb = RGBColor(30, 60, 114)
        para.add_run(f' {value}')
    
    # Executive Summary Section
    doc.add_heading('EXECUTIVE SUMMARY', level=2)
    
    summary_text = """25-year Global Logistics Expert with proven growth track record and strategic network assets. As a strategic leader with unique international connections, I have achieved verified performance across all global logistics sectors at Hanjin Shipping, including Americas/Europe sales, Americas/Asia/Middle East marketing pricing, and Eastern Europe regional expertise."""
    
    summary_para = doc.add_paragraph(summary_text)
    
    # Key Achievements
    doc.add_paragraph().add_run('Key Achievements:').bold = True
    achievements = [
        'Achieved #1 market share in Middle East routes',
        'Generated weekly operating profit of USD 1M+ during Iran sanctions, earning Ministry of Trade, Industry and Energy Award',
        'Grew customer fleet from 17 to 100+ vessels (700% increase)'
    ]
    
    for achievement in achievements:
        para = doc.add_paragraph(achievement, style='List Bullet')
    
    # Strategic Networks
    networks_para = doc.add_paragraph()
    networks_run = networks_para.add_run('Strategic Networks: ')
    networks_run.bold = True
    networks_para.add_run('Built exclusive competitive advantages through networks with Middle East key corporate executives, royalty/government officials, and EPC major corporation executives. Strategic partnerships with Sharaf Group and Globe Marine Group, along with ongoing collaborations with Hyundai Steel Industries, Samsung Heavy Industries, and Doosan Enerbility, represent immediately convertible business assets.')
    
    # WR Group Alignment
    alignment_para = doc.add_paragraph()
    alignment_run = alignment_para.add_run('WR Group Alignment: ')
    alignment_run.bold = True
    alignment_para.add_run('Possess competencies matching WR Group\'s Project Logistics expertise. Accumulated comprehensive TIC (Testing, Inspection, Certification) industry experience and hands-on European intermodal service experience through Slovakia/Czech operations during Hanjin tenure.')
    
    # 1st Year Target
    target_para = doc.add_paragraph()
    target_run = target_para.add_run('1st Year Target: ')
    target_run.bold = True
    target_para.add_run('Aiming for KRW 50 billion revenue to develop Korea branch as Asia strategic hub, combining German headquarters\' European network with my Asia-Middle East network to create new global EPC logistics industry standards.')
    
    # Education Section
    doc.add_heading('EDUCATION', level=2)
    
    education_info = [
        'Korea Maritime & Ocean University | Maritime Finance MBA | Mar 2018 - Mar 2020',
        'Pusan National University | Bachelor of Linguistics | Mar 1994 - Feb 2000'
    ]
    
    for edu in education_info:
        doc.add_paragraph(edu)
    
    # Certifications & Language Skills
    doc.add_heading('CERTIFICATIONS & LANGUAGE SKILLS', level=2)
    
    skills_info = [
        ('English:', 'Business Level (Conducting business operations in English at current position)'),
        ('German:', 'Basic conversational and reading ability (Studied as second language in high school and university elective. Currently challenging but expected to recover to basic conversational/reading level with short-term review)'),
        ('Driver\'s License:', 'Class 1 Regular')
    ]
    
    for label, value in skills_info:
        para = doc.add_paragraph()
        run1 = para.add_run(label)
        run1.bold = True
        run1.font.color.rgb = RGBColor(30, 60, 114)
        para.add_run(f' {value}')
    
    # International Experience
    doc.add_heading('INTERNATIONAL EXPERIENCE & MULTICULTURAL COLLABORATION', level=2)
    
    intl_exp = [
        '2011-2012: Dubai, UAE (Hanjin Shipping Deputy Branch Manager - Overseeing 10 Middle East countries)',
        '2004: Bratislava, Slovakia & Prague, Czech Republic (Regional Specialist)',
        '1999-2000: Melbourne, Australia (Language Study)'
    ]
    
    for exp in intl_exp:
        doc.add_paragraph(exp)
    
    # Awards & Recognition
    doc.add_heading('AWARDS & RECOGNITION', level=2)
    
    award_para = doc.add_paragraph()
    award_title = award_para.add_run('2015 Ministry of Trade, Industry and Energy Minister\'s Award')
    award_title.bold = True
    award_title.font.color.rgb = RGBColor(42, 82, 152)
    award_para.add_run('\nExport Promotion Category, Trade Security Day\nRecognized for outstanding contribution to Korea\'s trade security during Iran sanctions period')
    
    # Strategic Competitive Advantages
    doc.add_heading('STRATEGIC COMPETITIVE ADVANTAGES FOR WR GROUP KOREA SUCCESS', level=2)
    
    # 1. Proven Business Performance
    doc.add_heading('1. Proven Business Performance & Global Market Expertise', level=3)
    
    # Key Achievements subsection
    doc.add_paragraph().add_run('Key Achievements').bold = True
    key_achievements = [
        'Grew Korean customers\' BV-classed fleet from 17 to 100+ vessels (700% growth)',
        'Secured vessel order contracts for Qatar Gas North Field South Project (USD 10 billion EPC)',
        'Won Petronas Malaysia-Canada project vessel order contracts',
        'Expanding Middle East EPC projects through strategic partnership with Hyundai Steel Industries'
    ]
    
    for achievement in key_achievements:
        doc.add_paragraph(achievement, style='List Bullet')
    
    # Middle East EPC Project Experience
    doc.add_paragraph().add_run('Middle East EPC Project Experience').bold = True
    me_exp = [
        'Direct negotiation and contract execution with Middle East petrochemical mega-corporations including SABIC, Dubai Aluminum, Qatar Chemical',
        'Successfully secured entire annual import volume from Ethiopian Shipping Line'
    ]
    
    for exp in me_exp:
        doc.add_paragraph(exp, style='List Bullet')
    
    # Global Market Experience
    doc.add_paragraph().add_run('Global Market Experience').bold = True
    global_exp = [
        'Deep understanding of major markets through diverse route experience: Middle East, Americas, Europe, Northeast Asia',
        'Demonstrated crisis response capabilities by supporting customer exports with government permits even during Iran sanctions'
    ]
    
    for exp in global_exp:
        doc.add_paragraph(exp, style='List Bullet')
    
    # Professional Experience Section
    doc.add_heading('PROFESSIONAL EXPERIENCE (25 Years)', level=2)
    
    # Bureau Veritas Korea
    company_para = doc.add_paragraph()
    company_run = company_para.add_run('Bureau Veritas Korea')
    company_run.bold = True
    company_run.font.size = Pt(14)
    company_run.font.color.rgb = RGBColor(30, 60, 114)
    
    position_para = doc.add_paragraph()
    position_run = position_para.add_run('Marketing & Sales Director, Marine & Offshore')
    position_run.bold = True
    position_run.font.color.rgb = RGBColor(42, 82, 152)
    position_para.add_run(' | 2017 - Present')
    
    doc.add_paragraph('(Ships, marine structures, and EPC project-related inspection service customer acquisition marketing and sales)')
    
    # Key Achievements for Bureau Veritas
    doc.add_paragraph().add_run('Key Achievements').bold = True
    bv_achievements = [
        'Grew Korean customers\' BV-classed vessels from 17 to 100+ (700% growth)',
        'First-ever contract wins for Qatar Gas and Petronas projects in 2022 (first since company establishment)',
        'Built strategic relationships with domestic Big 3 shipyards and Busan shipowners'
    ]
    
    for achievement in bv_achievements:
        doc.add_paragraph(achievement, style='List Bullet')
    
    # Logistics Business Relevance
    doc.add_paragraph().add_run('Logistics Business Relevance').bold = True
    logistics_relevance = [
        'Deep understanding of Middle East/Europe/Asia large EPC project sites',
        'Professional network expertise in marine structures and project cargo safety/regulatory compliance',
        'Collaboration experience with Bureau Veritas Industry, Certification, and Commodities divisions'
    ]
    
    for relevance in logistics_relevance:
        doc.add_paragraph(relevance, style='List Bullet')
    
    # Add page break for better formatting
    doc.add_page_break()
    
    # Hanjin Shipping experiences (condensed for space)
    company_para = doc.add_paragraph()
    company_run = company_para.add_run('Hanjin Shipping')
    company_run.bold = True
    company_run.font.size = Pt(14)
    company_run.font.color.rgb = RGBColor(30, 60, 114)
    
    # Major positions at Hanjin Shipping
    hanjin_positions = [
        ('Assistant Manager~Manager, Asia Marketing Team | 2012 - 2016', 
         'Container Shipping Division - Middle East & Red Sea Routes Management',
         ['Achieved #1 market share in Asia-Middle East routes',
          'Generated weekly operating profit of USD 1M+ during Iran sanctions',
          'Company representative for IRA (Middle East Shipping Conference) and IRSA (Red Sea Shipping Conference)',
          'Received 2015 Ministry of Trade, Industry and Energy Minister\'s Award for Trade Security']),
        
        ('Deputy Branch Manager, UAE Branch | 2011 - 2012',
         'Managing 10 Middle East Countries',
         ['Developed and executed integrated marketing strategies for 10 Middle East and Red Sea countries',
          'Executed agency contracts with Sharaf Group and Globe Marine Group (continuing to present)',
          'Participated in Abu Dhabi Barakah nuclear plant project cargo transport',
          'Direct contracts with mega clients including SABIC, Qatar Chemical, Dubai Aluminum']),
        
        ('Assistant Manager, Americas Marketing Team | 2007 - 2011',
         'Asia↔Americas Routes Management',
         ['Asia↔Americas route service establishment, vessel deployment, regional headquarters P&L management',
          'Created and distributed multimodal transport route freight confirmation guidelines and tools for field sales personnel',
          'Multimodal transport route design and multimodal service optimization'])
    ]
    
    for position, description, achievements in hanjin_positions:
        position_para = doc.add_paragraph()
        position_run = position_para.add_run(position)
        position_run.bold = True
        position_run.font.color.rgb = RGBColor(42, 82, 152)
        
        if description:
            doc.add_paragraph(description)
        
        for achievement in achievements:
            doc.add_paragraph(achievement, style='List Bullet')
    
    # Business Plan Section
    doc.add_heading('BUSINESS PLAN & ASPIRATIONS POST-EMPLOYMENT', level=2)
    
    # Phase 1
    doc.add_heading('Phase 1 (Year 1): Immediate Execution Using Existing Networks', level=3)
    
    doc.add_paragraph().add_run('Confirmed Project Pipeline').bold = True
    
    # Year 1 Targets
    doc.add_paragraph().add_run('Year 1 Targets').bold = True
    year1_targets = [
        'Revenue: KRW 50 billion (200% achievement vs German headquarters target)',
        'Core Customers: 15 companies secured (5 EPC majors + 3 shipbuilders + 7 Middle East local companies)',
        'Differentiated Services: Complete multimodal/ESG eco-friendly logistics platform establishment'
    ]
    
    for target in year1_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # Phase 2
    doc.add_heading('Phase 2 (Years 2-3): Asia Strategic Hub Completion', level=3)
    
    # Years 2-3 Targets
    doc.add_paragraph().add_run('Years 2-3 Targets').bold = True
    years23_targets = [
        'Year 2 Revenue: KRW 90 billion (Asia regional hub completion)',
        'Year 3 Revenue: KRW 150 billion (Top-tier Asia EPC logistics company)',
        'Regional Expansion: Southeast Asia entry through Vietnam/Thailand/Indonesia hub establishment'
    ]
    
    for target in years23_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # Long-term Vision
    doc.add_heading('Long-term Vision: Global EPC Logistics Leader', level=3)
    
    doc.add_paragraph().add_run('5-Year Target').bold = True
    five_year_targets = [
        'Revenue KRW 300 billion: #1 Asia EPC logistics market share',
        'Regional Expansion: Asia-Pacific network encompassing Southeast Asia, India, Australia'
    ]
    
    for target in five_year_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # Conclusion
    conclusion_para = doc.add_paragraph()
    conclusion_run = conclusion_para.add_run('Conclusion: ')
    conclusion_run.bold = True
    conclusion_para.add_run('Based on 25 years of global logistics experience and exclusive network assets, I will develop WR Group Korea branch not as a simple local corporation but as a strategic growth engine encompassing all of Asia. Where WR Group\'s innovative vision meets my execution capabilities, we will together achieve historic performance creating new standards in the global EPC logistics industry.')
    
    # Final signature
    doc.add_paragraph()
    signature_para = doc.add_paragraph('September 2, 2025')
    signature_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    name_para = doc.add_paragraph('Sang Jin Han')
    name_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    name_run = name_para.runs[0]
    name_run.bold = True
    name_run.font.size = Pt(14)
    name_run.font.color.rgb = RGBColor(30, 60, 114)
    
    return doc

def main():
    """Main function to create and save the Word document"""
    try:
        # Create the document
        doc = create_resume_document()
        
        # Save the document
        output_path = 'SANG_JIN_HAN_Resume_WR_Group.docx'
        doc.save(output_path)
        
        print(f"✅ Resume successfully converted to Word document: {output_path}")
        print(f"📄 File saved in current directory: {os.path.abspath(output_path)}")
        
    except Exception as e:
        print(f"❌ Error creating Word document: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    main()