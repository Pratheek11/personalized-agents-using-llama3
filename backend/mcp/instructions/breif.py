llm_prompt = "Please provide a brief, clear, and easily understandable summary of the " \
"following prompt. Keep your response concise. If u are summarizing multiple prompts, " \
"summarize each one separately and add all summaries to the final response do not loose any." \
" Focus on the main topics and key points without unnecessary details." \
""\
" You are a helpful assistant who always responds in clean, readable Markdown." \
"Use:"\
"- **Bold** for important points"\
"- Bullet points or numbered lists for structure"\
"- Triple backticks for code blocks"\
"- Headers (like ## Summary) where appropriate"\
""\
"All output should be well-structured Markdown that is ready to be rendered in a frontend."

email_prompt = "Briefly summarize the key points from the user's email. You can ignore the spam and promotional emails. Focus on the main topics and any action items mentioned. If it is a reply, include the context of the original email. Keep the summary concise and to the point. If there are multiple emails, summarize each one separately. Also send the note if there are more than one mails from same sender."

meeting_prompt = "Briefly summarize the subject of the meeting and meeting scheduler name. If there are multiple meetings, summarize each one separately. If there are no meetings, return 'No meetings scheduled' for this particular summary. Keep the summary concise and to the point."

# 