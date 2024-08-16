completed_hwork=12
number_hours=1.5
name_course='Python'
time_1_task=number_hours/completed_hwork
#Вариант с соблюдением точного повторения пробелов
print("Курс: Python, всего задач:"+str(completed_hwork)+", затрачено часов:"+str(number_hours)+", среднее время выполнения",time_1_task,"часа.")
print("Курс: Python, всего задач:"+str(completed_hwork)+", затрачено часов:"+str(number_hours)+", среднее время выполнения "+str(time_1_task)+" часа.")
#Вариант без соблюдения точного повторения пробелов, но с учетом требования print(a, b, c)
print("Курс: Python, всего задач:",completed_hwork,", затрачено часов:",number_hours,", среднее время выполнения",time_1_task,"часа.")