import React, { useState } from 'react';

const TRANSLATIONS = {
  "en-US": {
    "meetingNotesSummary": "Meeting notes summary",
    "transformNotes": "Transform your raw meeting notes into a professional, structured summary",
    "rawMeetingNotes": "Raw meeting notes",
    "meetingNotes": "meeting notes",
    "transcripts": "transcripts",
    "bulletPoints": "bullet points",
    "placeholderText": "here...",
    "summarizing": "Summarizing...",
    "summarize": "Summarize",
    "clear": "Clear",
    "structuredSummary": "Structured summary",
    "summaryPlaceholder": "Your structured summary will appear here after you paste your meeting notes and click \"Summarize\".",
    "generatingSummary": "Generating summary...",
    "footerText": "Created with Claude - Transform your meeting notes into actionable summaries",
    "enterNotesError": "Please enter some meeting notes to summarize.",
    "summaryError": "An error occurred while generating the summary. Please try again.",
    "pasteYour": "Paste your",
    "or": "or",
    "summaryPrompt": "Please convert the following raw meeting notes into a well-structured summary. Format the summary to include:\n\n1. A brief overview of the meeting\n2. Key decisions made\n3. Action items with assignees and deadlines (if mentioned)\n4. Important discussion points\n5. Next steps or follow-up items\n\nPlease use clear headings and bullet points to make the summary easy to read and scan.\n\nRaw meeting notes:"
  },
  /* LOCALE_PLACEHOLDER_START */
  "es-ES": {
    "meetingNotesSummary": "Resumen de notas de reunión",
    "transformNotes": "Transforma tus notas de reunión en bruto en un resumen profesional y estructurado",
    "rawMeetingNotes": "Notas de reunión en bruto",
    "meetingNotes": "notas de reunión",
    "transcripts": "transcripciones",
    "bulletPoints": "puntos clave",
    "placeholderText": "aquí...",
    "summarizing": "Resumiendo...",
    "summarize": "Resumir",
    "clear": "Limpiar",
    "structuredSummary": "Resumen estructurado",
    "summaryPlaceholder": "Tu resumen estructurado aparecerá aquí después de pegar tus notas de reunión y hacer clic en \"Resumir\".",
    "generatingSummary": "Generando resumen...",
    "footerText": "Creado con Claude - Transforma tus notas de reunión en resúmenes accionables",
    "enterNotesError": "Por favor ingresa algunas notas de reunión para resumir.",
    "summaryError": "Ocurrió un error al generar el resumen. Por favor intenta de nuevo.",
    "pasteYour": "Pega tus",
    "or": "o",
    "summaryPrompt": "Por favor convierte las siguientes notas de reunión en bruto en un resumen bien estructurado. Formatea el resumen para incluir:\n\n1. Una breve descripción general de la reunión\n2. Decisiones clave tomadas\n3. Elementos de acción con asignados y fechas límite (si se mencionan)\n4. Puntos de discusión importantes\n5. Próximos pasos o elementos de seguimiento\n\nPor favor usa encabezados claros y puntos clave para hacer el resumen fácil de leer y escanear.\n\nNotas de reunión en bruto:"
  }
  /* LOCALE_PLACEHOLDER_END */
};

const appLocale = '{{APP_LOCALE}}';
const browserLocale = navigator.languages?.[0] || navigator.language || 'en-US';
const findMatchingLocale = (locale) => {
  if (TRANSLATIONS[locale]) return locale;
  const lang = locale.split('-')[0];
  const match = Object.keys(TRANSLATIONS).find(key => key.startsWith(lang + '-'));
  return match || 'en-US';
};
const locale = (appLocale !== '{{APP_LOCALE}}') ? findMatchingLocale(appLocale) : findMatchingLocale(browserLocale);
const t = (key) => TRANSLATIONS[locale]?.[key] || TRANSLATIONS['en-US'][key] || key;

// Simple markdown renderer with proper CSS styling
const MarkdownRenderer = ({ content }) => {
  const styles = `
    h1 { font-size: 24px; font-weight: 600; margin: 12px 0 8px 0; color: #374528; }
    h2 { font-size: 20px; font-weight: 600; margin: 10px 0 6px 0; color: #374528; }
    h3 { font-size: 18px; font-weight: 600; margin: 8px 0 5px 0; color: #374528; }
    strong { font-weight: 600; }
    ul { margin: 8px 0; padding-left: 24px; }
    ol { margin: 8px 0; padding-left: 24px; }
    li { margin: 3px 0; }
    ul li { list-style-type: disc; }
    ul ul li { list-style-type: circle; }
    ul ul ul li { list-style-type: square; }
    ol li { list-style-type: decimal; }
    p { margin: 8px 0; }
    table { border-collapse: collapse; margin: 12px 0; width: 100%; }
    th { border: 1px solid #7a947a; padding: 8px 12px; background-color: #C4DDAB; font-weight: 600; text-align: left; }
    td { border: 1px solid #7a947a; padding: 8px 12px; text-align: left; }
    tr:nth-child(even) td { background-color: #f9f9f9; }
  `;
  
  const renderMarkdown = (text) => {
    let html;
    
    // Handle tables first
    html = text.replace(/\|.*?\|.*?\|\n\|(?:[-:])+?\|.*?\|\n((?:\|.*?\|.*?\|\n)*)/g, (match) => {
      const lines = match.trim().split('\n');
      let tableHtml = '<table>\n';
      
      // Process header row
      const headerCells = lines[0].split('|').slice(1, -1).map(cell => cell.trim());
      tableHtml += '<thead>\n<tr>';
      headerCells.forEach(cell => {
        tableHtml += `<th>${cell}</th>`;
      });
      tableHtml += '</tr>\n</thead>\n';
      
      // Skip the separator line and process body rows
      tableHtml += '<tbody>\n';
      for (let i = 2; i < lines.length; i++) {
        if (lines[i].trim()) {
          const cells = lines[i].split('|').slice(1, -1).map(cell => cell.trim());
          tableHtml += '<tr>';
          cells.forEach(cell => {
            tableHtml += `<td>${cell}</td>`;
          });
          tableHtml += '</tr>\n';
        }
      }
      tableHtml += '</tbody>\n</table>';
      
      return tableHtml;
    });
    
    // Handle headers
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.*?)$/gm, '<h1>$1</h1>');
    
    // Handle bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Process lists with proper nesting
    const lines = html.split('\n');
    const processedLines = [];
    let listStack = [];
    
    for (let line of lines) {
      // Detect list items (bullets or numbered)
      const bulletMatch = line.match(/^(\s*)[-*+] (.+)$/);
      const numberMatch = line.match(/^(\s*)\d+\.\s(.+)$/);
      
      if (bulletMatch || numberMatch) {
        const match = bulletMatch || numberMatch;
        const indentLevel = Math.floor(match[1].length / 2); // Calculate indent level
        const content = match[2];
        const listType = bulletMatch ? 'ul' : 'ol';
        
        // Close nested lists if we're going back to a previous level
        while (listStack.length > indentLevel + 1) {
          const closingTag = listStack.pop();
          processedLines.push(`</${closingTag}>`);
        }
        
        // Open new list if needed
        if (listStack.length === indentLevel) {
          processedLines.push(`<${listType}>`);
          listStack.push(listType);
        }
        
        // Add list item
        processedLines.push(`<li>${content}</li>`);
      } else {
        // Close all open lists when encountering non-list content
        while (listStack.length > 0) {
          const closingTag = listStack.pop();
          processedLines.push(`</${closingTag}>`);
        }
        
        // Handle other content
        if (line.trim() === '') {
          processedLines.push('<br />');
        } else if (!line.match(/^<[^>]+>/)) {
          processedLines.push(`<p>${line}</p>`);
        } else {
          processedLines.push(line);
        }
      }
    }
    
    // Close any remaining open lists
    while (listStack.length > 0) {
      const closingTag = listStack.pop();
      processedLines.push(`</${closingTag}>`);
    }
    
    html = processedLines.join('');
    
    return html;
  };

  return (
    <>
      <style>{styles}</style>
      <div
        dangerouslySetInnerHTML={{ __html: renderMarkdown(content) }}
      />
    </>
  );
};

const MeetingNotesSummary = () => {
  const [rawNotes, setRawNotes] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  // Sample examples for different types of notes
  const examples = {
    meetingNotes: `Product Planning Meeting - January 15, 2025

Attendees: Sarah (PM), Mike (Eng), Jennifer (Design), Alex (Marketing)

Agenda:
- Review Q1 roadmap
- Discuss new feature proposals
- Budget allocation for design resources

Key Points:
- Need to prioritize mobile app update
- Sarah suggested pushing analytics dashboard to Q2
- Mike raised concerns about API rate limits
- Jennifer presented new UI mockups
- Alex confirmed marketing budget of $50k for launch

Action Items:
- Sarah: Finalize feature prioritization by Jan 20
- Mike: Investigate API scalability options
- Jennifer: Revise mockups based on feedback
- Alex: Prepare campaign timeline

Next Meeting: January 22, 2025`,

    transcripts: `[00:00] Hey everyone, thanks for joining today's team standup.

[00:15] John: Alright, let's start with our progress updates. Sarah, how's the dashboard project coming along?

[00:25] Sarah: Great! I've completed the user authentication module and I'm about 80% done with the reporting interface. I should have the first draft ready for review by Thursday.

[00:40] John: Excellent. Any blockers I should know about?

[00:45] Sarah: Actually, yes. I'm having trouble with the data visualization library. The charts aren't rendering properly in dark mode.

[01:00] Mike: I can help with that. I had the same issue last month and found a workaround. Let's sync after this meeting.

[01:15] John: Perfect. Mark, what's your status on the mobile app update?

[01:25] Mark: We've pushed the new UI to staging yesterday. QA is testing it now. Found a few minor bugs but nothing critical. Should be good to deploy on Friday.

[01:40] John: Sounds like we're on track. Everyone, remember our sprint review is on Wednesday at 2 PM. Please have your demos ready.`,

    bulletPoints: `• Weekly All-Hands Meeting Overview
  - Company Q4 performance review
  - New hire announcements
  - Office renovation update
  
• Quarterly OKRs Review
  ✓ Revenue target: 12% above goal
  ✓ Customer satisfaction: 4.8/5.0 rating
  ✗ Team expansion: 2 positions still unfilled
  
• Product Updates
  - Mobile app downloads up 25%
  - Premium subscription conversion rate: 8.2%
  - Bug fix deployment scheduled for tomorrow
  
• Action Items
  1. HR to post remaining job openings by end of week
  2. Finance to prepare Q1 budget proposal
  3. Engineering to conduct post-mortem on last week's outage
  4. Marketing to launch social media campaign on Monday
  
• Upcoming Deadlines
  - Q1 planning document: February 1st
  - Performance reviews: February 15th
  - Team building event: February 28th`
  };

  const loadExample = (type) => {
    setRawNotes(examples[type]);
    setSummary('');
    setError('');
  };

  const handleSummarize = async () => {
    if (!rawNotes.trim()) {
      setError(t('enterNotesError'));
      return;
    }

    setIsLoading(true);
    setError('');
    setSummary('');

    try {
      // Create a prompt for Claude to generate a structured summary
      const prompt = `
        ${t('summaryPrompt')}
        ${rawNotes}
        
        Please respond in ${locale} language
      `;

      const response = await window.claude.complete(prompt);
      setSummary(response);
    } catch (err) {
      setError(t('summaryError'));
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setRawNotes('');
    setSummary('');
    setError('');
  };

  return (
    <div style={{ 
      fontFamily: 'Inter, sans-serif',
      minHeight: '100vh',
      backgroundColor: '#C4DDAB',
      padding: '40px',
      color: '#374528'
    }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        {/* Header */}
        <header style={{ marginBottom: '40px' }}>
          <h1 style={{ 
            fontSize: '32px', 
            fontWeight: '600', 
            margin: '0 0 10px 0',
            color: '#374528'
          }}>
            {t('meetingNotesSummary')}
          </h1>
          <p style={{ fontSize: '16px', color: '#5a6b4a', margin: '0' }}>
            {t('transformNotes')}
          </p>
        </header>

        {/* Main Content */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '40px' }}>
          {/* Input Section */}
          <div>
            <h2 style={{ 
              fontSize: '20px', 
              fontWeight: '500', 
              marginBottom: '16px',
              color: '#374528'
            }}>
              {t('rawMeetingNotes')}
            </h2>
            <div style={{ position: 'relative' }}>
              <textarea
                value={rawNotes}
                onChange={(e) => setRawNotes(e.target.value)}
                placeholder=" "
                style={{
                  width: '100%',
                  height: '280px',
                  padding: '16px',
                  borderRadius: '8px',
                  border: '1px solid #7a947a',
                  backgroundColor: 'white',
                  fontSize: '14px',
                  color: '#374528',
                  resize: 'vertical',
                  marginBottom: '16px',
                  lineHeight: '1.6'
                }}
              />
              {!rawNotes && (
                <div style={{
                  position: 'absolute',
                  top: '16px',
                  left: '16px',
                  pointerEvents: 'none',
                  color: '#7a947a',
                  fontSize: '14px',
                  lineHeight: '1.6'
                }}>
                  {t('pasteYour')}{' '}
                  <button
                    onClick={() => loadExample('meetingNotes')}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#374528',
                      textDecoration: 'underline',
                      cursor: 'pointer',
                      fontSize: '14px',
                      padding: '0',
                      pointerEvents: 'auto'
                    }}
                  >
                    상세 회의록
                  </button>
                  {', '}
                  <button
                    onClick={() => loadExample('transcripts')}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#374528',
                      textDecoration: 'underline',
                      cursor: 'pointer',
                      fontSize: '14px',
                      padding: '0',
                      pointerEvents: 'auto'
                    }}
                  >
                    회의 전사록
                  </button>
                  {', '}{t('or')}{' '}
                  <button
                    onClick={() => loadExample('bulletPoints')}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#374528',
                      textDecoration: 'underline',
                      cursor: 'pointer',
                      fontSize: '14px',
                      padding: '0',
                      pointerEvents: 'auto'
                    }}
                  >
                    전략회의 노트
                  </button>
                  {' '}{t('placeholderText')}
                </div>
              )}
            </div>
            <div style={{ display: 'flex', gap: '12px' }}>
              <button
                onClick={handleSummarize}
                disabled={isLoading}
                style={{
                  padding: '12px 24px',
                  borderRadius: '8px',
                  border: 'none',
                  backgroundColor: '#374528',
                  color: 'white',
                  fontSize: '16px',
                  fontWeight: '500',
                  cursor: isLoading ? 'not-allowed' : 'pointer',
                  opacity: isLoading ? 0.7 : 1,
                  transition: 'opacity 0.2s'
                }}
              >
                {isLoading ? t('summarizing') : t('summarize')}
              </button>
              <button
                onClick={handleClear}
                style={{
                  padding: '12px 24px',
                  borderRadius: '8px',
                  border: '1px solid #374528',
                  backgroundColor: 'transparent',
                  color: '#374528',
                  fontSize: '16px',
                  fontWeight: '500',
                  cursor: 'pointer'
                }}
              >
                {t('clear')}
              </button>
            </div>
          </div>

          {/* Output Section */}
          <div>
            <h2 style={{ 
              fontSize: '20px', 
              fontWeight: '500', 
              marginBottom: '16px',
              color: '#374528'
            }}>
              📝 완성된 회의록 (2-3장 분량)
            </h2>
            <div style={{
              minHeight: '400px',
              padding: '16px',
              borderRadius: '8px',
              backgroundColor: 'white',
              border: '1px solid #7a947a',
              fontSize: '14px',
              lineHeight: '1.6',
              whiteSpace: 'pre-wrap',
              position: 'relative',
              maxHeight: '80vh',
              overflowY: 'auto'
            }}>
              {summary && !isLoading && !error && (
                <div style={{ color: '#374528' }}>
                  <MarkdownRenderer content={summary} />
                </div>
              )}
              {!summary && !isLoading && !error && (
                <div style={{ 
                  color: '#7a947a', 
                  fontStyle: 'italic',
                  position: 'absolute',
                  top: '16px',
                  left: '16px'
                }}>
                  {t('summaryPlaceholder')}
                  <br /><br />
                  <strong style={{ color: '#5a6b4a' }}>💡 팁:</strong>
                  <br />• 사전 참고 내용만으로도 회의록 작성 가능
                  <br />• 미팅 협의 내용만으로도 회의록 작성 가능  
                  <br />• 두 내용을 모두 입력하면 가장 완전한 회의록 생성
                </div>
              )}
              {error && (
                <div style={{ color: '#d73a49', marginBottom: '16px' }}>
                  {error}
                </div>
              )}
              {isLoading && (
                <div style={{ 
                  color: '#5a6b4a',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px'
                }}>
                  <div style={{
                    width: '20px',
                    height: '20px',
                    border: '2px solid #C4DDAB',
                    borderTop: '2px solid #374528',
                    borderRadius: '50%',
                    animation: 'spin 1s linear infinite'
                  }} />
                  상세한 회의록을 작성하고 있습니다...
                  <style>
                    {`
                      @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                      }
                    `}
                  </style>
                </div>
              )}
            </div>
            
            {/* Summary Stats */}
            {summary && (
              <div style={{
                marginTop: '12px',
                padding: '12px',
                backgroundColor: '#f8f9f7',
                borderRadius: '6px',
                fontSize: '12px',
                color: '#5a6b4a',
                display: 'flex',
                justifyContent: 'space-between'
              }}>
                <span>📊 문자 수: {summary.length.toLocaleString()}</span>
                <span>📄 예상 페이지: {Math.ceil(summary.length / 2000)}장</span>
                <span>⏱️ 예상 읽기 시간: {Math.ceil(summary.length / 1000)}분</span>
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <footer style={{ 
          marginTop: '60px', 
          paddingTop: '20px',
          borderTop: '1px solid #7a947a',
          textAlign: 'center', 
          color: '#5a6b4a',
          fontSize: '14px'
        }}>
          {t('footerText')}
        </footer>
      </div>
    </div>
  );
};

export default MeetingNotesSummary;