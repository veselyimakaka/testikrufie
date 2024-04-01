from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

app = QApplication ([])
window = QWidget()
window.resize(1200, 800)
window.setWindowTitle('Тестик Руфье для бибизян')

hello_text = QLabel (
    'Это тест для определения работоспособности серда. НЕ является инструментом для постановки диагноза. Пжешка, следуйте инструкциям'
    )

age_text = QLabel ('Введите возраст:')
age_input = QLineEdit()

pre_peace_text = QLabel('Сохраняйте спокойствие :)')

peace_text = QLabel('Введите пульс в состоянии покоя:')
peace_input = QLineEdit()



physical_text = QLabel('Сделайте 30 приседаний за 45 секунд')

post_physical_text = QLabel('Введите пульс после физнагрузки')
post_physical_input = QLineEdit()


rest_text = QLabel ('Отдохните 30 секунд')

post_rest_text = QLabel ('Введите пульс после реста')
post_rest_input = QLineEdit()


btn = QPushButton ('Анализ')

result_area = QGroupBox('Результат тестика')
index_text = QLabel ('Индекс Руфье:')
index = QLabel ('~')

description = QLabel ('~~')

main_line =QHBoxLayout()
left_col = QVBoxLayout()
right_col = QVBoxLayout()
row1 = QHBoxLayout()
row1.addStretch(1)
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()
result_line = QVBoxLayout()

row1.addWidget(age_text, alignment = Qt.AlignLeft)
row1.addWidget(age_input, alignment = Qt.AlignLeft)

row2.addWidget(peace_text)
row2.addWidget(peace_input)

row3.addWidget(post_physical_text)
row3.addWidget(post_physical_input)

row4.addWidget(post_rest_text)
row4.addWidget(post_rest_input)

left_col.addWidget(hello_text)
left_col.addLayout(row1)
left_col.addWidget(pre_peace_text)
left_col.addLayout(row2)
left_col.addWidget(physical_text)
left_col.addLayout(row3)
left_col.addWidget(rest_text)
left_col.addLayout(row4)
left_col.addWidget(btn)

result_line.addWidget(index_text)
result_line.addWidget(index)
result_line.addWidget(description)
result_area.setLayout(result_line)

right_col.addWidget(result_area)

main_line.addLayout(left_col)
main_line.addLayout(right_col)
window.setLayout(main_line)

window.setStyleSheet('font-size: 24px;')



def rufier():
    age = int(age_input.text())
    p1 = int(peace_input.text())
    p2 = int(post_physical_input.text())
    p3 = int(post_rest_input.text())
    print(age,p1,p2,p3)
    rufier_index = (4 * (p1 + p2 + p3)- 200)/ 10
    index.setText(str(rufier_index))
    if age >= 15:
        if rufier_index >= 15:
            description.setText('Низкая работоспособность сердца')
        elif rufier_index < 15 and rufier_index >= 11:
            description.setText('Удовлетворительная работоспособность сердца')
        elif rufier_index < 11 and rufier_index >= 6:
            description.setText('Средняя работоспособность сердца')
        elif rufier_index < 6 and rufier_index >= 0.5:
            description.setText('Работоспособность сердца выше среднего')
        elif rufier_index <= 0.4:
            description.setText('Высокая работоспособность сердца')

    

btn.clicked.connect(rufier)


window.show()
app.exec()
