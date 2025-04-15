import csv
from db import create_connection, fetch_result
from utils.cli_styles import success_msg, error_msg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_tasks():
    fetch_query = "SELECT * FROM tasks"

    try:
        connection = create_connection()
        tasks = fetch_result(connection, fetch_query)

        if tasks:
            # ─── CSV Export ───────────────────────────────────────
            with open('tasks_export.csv', 'w', newline='') as csvfile:
                fieldnames = ['Task ID', 'User ID', 'Title', 'Description', 'Date', 'Priority', 'Status']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for task in tasks:
                    writer.writerow({
                        'Task ID': task[0],
                        'User ID': task[1],
                        'Title': task[2],
                        'Description': task[3],
                        'Date': task[4],
                        'Priority': task[5],
                        'Status': task[6]
                    })

            # ─── PDF Export ───────────────────────────────────────
            pdf = canvas.Canvas("tasks_export.pdf", pagesize=letter)
            width, height = letter
            y = height - 50

            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y, "TaskPro — Exported Tasks")
            y -= 30
            pdf.setFont("Helvetica", 10)

            for task in tasks:
                pdf.drawString(50, y, f"📝 Task ID     : {task[0]}")
                y -= 15
                pdf.drawString(50, y, f"👤 User ID     : {task[1]}")
                y -= 15
                pdf.drawString(50, y, f"📌 Title       : {task[2]}")
                y -= 15
                pdf.drawString(50, y, f"🧾 Description : {task[3]}")
                y -= 15
                pdf.drawString(50, y, f"📅 Date        : {task[4]}")
                y -= 15
                pdf.drawString(50, y, f"🔥 Priority    : {task[5]}")
                y -= 15
                pdf.drawString(50, y, f"📍 Status      : {task[6]}")
                y -= 30

                # New page if content overflows
                if y < 100:
                    pdf.showPage()
                    y = height - 50
                    pdf.setFont("Helvetica", 10)

            pdf.save()

            print(success_msg("\t✔ Tasks exported successfully to 'tasks_export.csv' and 'tasks_export.pdf'"))
        else:
            print(error_msg("\t✘ No tasks available to export."))

    except Exception as e:
        print(error_msg(f"\t✘ Error: {e}"))

    finally:
        connection.close()