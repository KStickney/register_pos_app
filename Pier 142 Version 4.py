# Pier 142 POS System Version 4

# Clear everything whenever click out of something - make one function (or several smaller ones depending on which
# button clicked)

# self.stylesheet = """
# QPushButton{
# background-color:#434343;
# color: #ffffff;
# }
# QMainWindow{}
# QPushButton#SomeName{}
# """
# self.setStyleSheet()
# button.setObjectName("SomeName")

import sys, traceback, os
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMenu

import Pier_142_Excel as pexc
#TODO Add fulfilled method and save to excel

#department_menu = [['Milkshake', 3], ['Smoothie', 3], ['Coffee', 2], ['Sandwich', 4]]

#flavor_menu = [
    #[['Vanilla', 0], ['Chocolate', 0], ['Strawberry', 0], ['Caramel', 0], ['Oreo', 0], ['Thin Mint', 0], ['Samoa', 0]],
    #[['Tropical', 0],['Special', 0], ['Custom', 0]],
    #[['Cold Brew', 0]],
    #[['Hot Pocket', 0]]]

#extras_menu = [
    #[['Chocolate Syrup', 0], ['Caramel', 0], ['Oreo', 0], ['Thin Mint', 0], ['PB', 0], ['Protein', 0], ['No whip', 0]],
    #[[['Strawberries', 0], ['Mangoes', 0], ['Peaches', 0], ['Pineapple', 0], ['Blueberries', 0]],
     #[['Fruit Punch', 0], ['Passion Fruit',0]]],
    #[[['Almond Milk', 1], ["Whole Milk", 0]],[['',0]]],
    #[['',0]]
#]

#label_menu = [
   # ['Type:','Extras:'],
    #['Type:','Fruit:','Juice:'],
   # ['Type:','Milk:',''],
   # ['Type:','']
#]

Qheight = 400
Qwidth = 40

order_height = 400
order_width = 50

mini_window_factor = .90

MAX_COL = 5 #max number of flavors/extras in column

ORDER_GRID_ROW = 2
ORDER_GRID_COL = 5




class Register(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pier 142 Register")

        # CHange for WHEN HAVE MULTIPLE SCREENS??
        self.screen = app.primaryScreen()
        self.swidth = self.screen.size().width()
        self.sheight = self.screen.size().height()

        # self.setStyleSheet("background-color: white;")

        cart_btn_height = 20
        cart_btn_width = 100

        self.stylesheet = f"""
        QWidget>QMainWindow{{
            background-color: purple;
        }}
        
        #QPushButton{{
            border-radius: 20px;
        }}
        
        QPushButton#department-menu{{
            background-color: rgba(255,215,181,0.8);
            border-style: outset;
            border-width: 2px;
            border-radius: 20px;
            border-color: black;
            padding: 4px;
            font: bold 18px;
        }}

        QPushButton#department-menu:checked{{
            background-color: rgba(46,89,132,0.6);
            border-style: inset;
            color: white;
        }}

        QPushButton#extra-menu{{
            background-color: rgba(10,52,97,.2);
            border-style: outset;
            border-width: 1px;
            border-radius: 10px;
            border-color: grey;
            padding: 0px;
            font: bold 15px;
            max-height: {150}px;
            min-height: {150}px;
            max-width: {235}px;
            min-width: {150}px;

        }}
        
        QPushButton#extra-menu:checked:!pressed{{
            color: white;
            background-color: rgba(20,100,20,.3);
            border-color: grey;
        }}
        QLabel#excess{{
            max-height: {150}px;
            min-height: {150}px;
            max-width: {235}px;
            min-width: {150}px;
        }}
        
        QLabel#extra-menu{{
            font: bold 14px;
            max-width: 150px;
        }}
        QLabel#flavor-menu{{
            font: bold 14px;
            max-width: 150px;
        }}

        QPushButton#department-submit{{
            background-color: rgba(247,216,186,0.6);
            border-style: outset;
            border-width: 1px;
            border-radius: 10px;
            border-color: grey;
            padding: 0px;
            font: bold 12px;
            max-height: {30}px;
            min-height: {30}px;
        }}
        QPushButton#department-submit:pressed{{
            color: white;
            background-color: rgba(238,36,20,.7);
            border-color: grey;
        }}
        
        
        QPushButton#cart-submit{{
            background-color: rgba(47,77,97,.8);
            border-style: outset;
            border-width: 1px;
            border-radius: 15px;
            border-color: grey;
            padding: 0px;
            font: bold 12px;
            max-height: {35}px;
            min-height: {35}px;
            max-width: 400px;
        }}
        QPushButton#cart-submit:pressed{{
            color: white;
            background-color: rgba(20,100,20,.4);
            border-color: grey;
        }}


        QLabel#cart-total-price{{
            font: bold 16px;
        }}

        QLabel#cart-main-label{{
            font: bold 14px;
        }}
        
        QLabel#cart-total{{
            font: bold 16px;
        }}
        
        QLabel#cart-item{{
            font: bold 14px
        }}
        
        QPushButton#cart-button{{
            background-color: rgba(151,35,40,0.8);
            color: black;
            border-style: outset;
            border-width: 1px;
            border-radius: 10px;
            border-color: black;
            padding: 0px;
            font: bold 12px;
            max-height: {cart_btn_height}px;
            max-width: {cart_btn_width}px;
            min-height: {cart_btn_height}px;
            min-width: {cart_btn_width}px;
            backgrounds: qradialgradient(
            cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
            radius: 1.35, stop: 0 #fff, stop: 1 #888
            );
        }}
        QPushButton#cart-button:pressed{{
            background-color: purple;
            color: white;
        }}
        
        QLabel#cart-quantity{{
            font: bold 14px;
            max-height: {cart_btn_height}px;
            max-width: {cart_btn_width};
            min-height: {cart_btn_height};
            min-width: {cart_btn_width};
        }}
        
        QLabel#cart-total-quantity{{
            font: bold 16px;
            max-height: {cart_btn_height};
            max-width: {cart_btn_width};
            min-height: {cart_btn_height};
            min-width: {cart_btn_width};
        }}
        
        QLabel#cart-align{{
            max-height: {cart_btn_height};
            max-width: {cart_btn_width};
            min-height: {cart_btn_height};
            min-width: {cart_btn_width};
        }}
        
        
        QMenu::item{{
            background-color: black;
            color: purple
        }}

        QLineEdit, QTextEdit{{
            border: 1.4px solid black;
            border-radius: 5px;
            padding: 0 8px;
            background: white;
        }}
        
        QScrollArea{{
            background: transparent;
            background-color:transparent;
        }}
        QScrollArea>QWidget>QWidget{{
            background: transparent;
        }}
        #QScrollArea>QWidget>QScrollBar{{
            background: rgb(240,240,240);
        }}
        
        QScrollArea>QWidget>QScrollBar{{
            background: rgb(240,240,240);
        }}
        QScrollBar::handle{{
            background: rgb(205,205,205)
        }}
        QScrollBar::handle:pressed{{
            background: gray;
        }}
        QScrollBar::handle:hover{{
            background: gray;
        }}
        
        QSpinBox{{
            border: 1px solid black;
            border-radius: 5px;
            min-height: 25px;
        }}

        #QMainWindow{{
            background-color:grey;
        }}
        
        
        
        """
        self.setStyleSheet(self.stylesheet)

        self.UIComponents()
        # self.showMaximized()

    def UIComponents(self):

        self.set_stacked_widget()

        self.Qcenter = int(self.swidth / 2 - Qheight / 2)

        # NEW CODE

        self.name_box = QLineEdit()
        self.name_box.setPlaceholderText('Customer Name')
        # self.name_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.name_box.setMinimumSize(100, 50)

        # Department Grid
        self.department_grid = QHBoxLayout()
        for item in department_menu:
            try:
                self.department_grid.addWidget(QPushButton(QIcon('./images/'+item[0]+'.png'),item[0], self))
            except:
                self.department_grid.addWidget(QPushButton(item[0], self))

        self.department_grid_count = self.department_grid.count()
        for j in range(self.department_grid.count()):
            # self.department_grid.itemAt(j).widget().setAutoExclusive(True)
            self.department_grid.itemAt(j).widget().setCheckable(True)
            self.department_grid.itemAt(j).widget().clicked.connect(lambda: self.department_clicked())
            self.department_grid.itemAt(j).widget().setMinimumSize(100, 100)
            self.department_grid.itemAt(j).widget().setMaximumSize(400, 100)
            self.department_grid.itemAt(j).widget().setObjectName('department-menu')
            # self.department_grid.itemAt(j).widget().setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            # self.department_grid.itemAt(j).widget().resize(40,40)

            self.department_grid.itemAt(j).widget().setIconSize(QtCore.QSize(100, 100))
            # self.department_grid.itemAt(j).widget().setIconSize(self.size())
            # name = self.department_grid.findChild(QPushButton, 0)

        # Notes Box
        # self.notes_box = QTextEdit(self)
        # self.notes_box.setGeometry(self.Qcenter,250,Qheight,200)
        # self.notes_box.setPlaceholderText('Notes')
        # self.notes_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Submit Button
        # self.cart_button = QPushButton("Cart",self)
        # self.submit_button.setGeometry(self.Qcenter,500,Qheight,Qwidth)
        # self.cart_button.clicked.connect(self.open_cart)
        # self.cart_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Register Grid - Added
        self.register_grid = QVBoxLayout()
        # self.register_grid.setContentsMargins(400,0,400,300)####change to resize
        self.register_grid.setSpacing(10)

        self.register_grid.addWidget(self.name_box)
        self.register_grid.addLayout(self.department_grid)
        # self.register_grid.addWidget(self.notes_box)
        # self.register_grid.addWidget(self.cart_button)



        self.outer_layer = QVBoxLayout()
        self.outer_layer.addLayout(self.register_grid)  # stretch=1)
        scroll = QScrollArea()
        scroll.setWidget(self.department_widget)
        scroll.setWidgetResizable(True)
        #self.outer_layer.addWidget(self.department_widget)
        self.outer_layer.addWidget(scroll)

        #self.outer_layer.addLayout(self.order_status_layer)  # ,80)
        #self.outer_layer.addLayout(self.completed_orders_grid)
        self.setLayout(self.outer_layer)



    def department_clicked(self):
        button = self.sender()
        index = self.department_grid.indexOf(button)

        if not button.isChecked():  ## what happens if user is unchecking box
            self.department_widget.setCurrentIndex(0)

        else:
            for i in range(self.department_grid.count()):
                if i != index:
                    self.department_grid.itemAt(i).widget().setChecked(False)

            self.isDepartmentLayer = True
            self.department_widget.setCurrentIndex(index + 1)

    def set_stacked_widget(self):
        max_w = 200
        max_h = 100

        self.department_widget = QStackedWidget()

        # Cart
        self.cart_widget = QWidget()
        self.department_widget.addWidget(self.cart_widget)  # Add dummy cart widget
        self.update_cart()

        try:
            self.department_widgets = []
            self.extras_menus = []
            for index in range(len(department_menu)):
                self.extras_menus.append([])

                widget = QWidget()

                grid_layout = QGridLayout()

                flavor_label = QLabel(label_menu[index][0], self)
                flavor_label.setMaximumSize(max_w, max_h)
                flavor_label.setObjectName('flavor-menu')
                grid_layout.addWidget(flavor_label,0,0)

                try:
                    i = 0
                    j = 1
                    for item in flavor_menu[index]:
                        btn = QPushButton(item[0], self)
                        try:
                            btn.setIcon(QIcon("./images/"+item[0]+".png"))
                            btn.setIconSize(QtCore.QSize(100,100))
                        except:
                            pass
                        btn.setObjectName('extra-menu')
                        if grid_layout.itemAtPosition(i, MAX_COL) is None:
                            grid_layout.addWidget(btn, i, j)
                        else:
                            i += 1
                            j = 1
                            label = QLabel("", self)
                            label.setMaximumSize(max_w, max_h)
                            label.setObjectName('flavor-menu')
                            grid_layout.addWidget(label, i, 0)
                            grid_layout.addWidget(btn, i, j)
                        j += 1

                    if grid_layout.columnCount() != (MAX_COL+1): #Adding extra spaces so keep alignment the same
                        for i in range(1,MAX_COL+1):
                            if grid_layout.itemAtPosition(0,i) is None:
                                label = QLabel("")
                                label.setObjectName("excess")
                                grid_layout.addWidget(label,0,i)
                except Exception as e:
                    print(384,e)

                try:
                    if type(extras_menu[index][0][0]) == list:
                        i = grid_layout.rowCount()
                        k=1
                        for layer in extras_menu[index]:
                            try:
                                label = QLabel(label_menu[index][k])
                                label.setMaximumSize(max_w,max_h)
                                label.setObjectName('extra-menu')
                                grid_layout.addWidget(label,i,0)
                            except Exception as e:
                                print(395,e)
                            j=1
                            for obj in layer:
                                if obj[0] == '':
                                    break
                                btn = QPushButton(obj[0], self)
                                try:
                                    btn.setIcon(QIcon("./images/" + obj[0] + ".png"))
                                    btn.setIconSize(QtCore.QSize(100, 100))
                                except:
                                    pass
                                btn.setObjectName('extra-menu')
                                if grid_layout.itemAtPosition(i, MAX_COL) is None:
                                    grid_layout.addWidget(btn,i,j)
                                else:
                                    i += 1
                                    j = 1
                                    label = QLabel("", self)
                                    label.setMaximumSize(max_w, max_h)
                                    label.setObjectName('extra-menu')
                                    grid_layout.addWidget(label, i, 0)
                                    grid_layout.addWidget(btn, i, j)

                                j += 1
                            i+=1
                            k+=1

                    else:
                        try:
                            i = grid_layout.rowCount()
                            label = QLabel(label_menu[index][1])
                            label.setMaximumSize(max_w, max_h)
                            label.setObjectName('extra-menu')
                            grid_layout.addWidget(label, i, 0)
                            j=1
                            for obj in extras_menu[index]:
                                if obj[0]=='':
                                    break
                                try:
                                    btn = QPushButton(obj[0], self)
                                    try:
                                        btn.setIcon(QIcon("./images/" + obj[0] + ".png"))
                                        btn.setIconSize(QtCore.QSize(100, 100))
                                    except:
                                        pass
                                    btn.setObjectName('extra-menu')
                                    if grid_layout.itemAtPosition(i, MAX_COL) is None:
                                        grid_layout.addWidget(btn, i, j)

                                    else:
                                        i += 1
                                        j = 1
                                        label = QLabel("", self)
                                        label.setMaximumSize(max_w, max_h)
                                        label.setObjectName('extra-menu')
                                        grid_layout.addWidget(label, i, 0)
                                        grid_layout.addWidget(btn, i, j)
                                    j+=1

                                except Exception as e:
                                    print(439,e)
                        except Exception as e:
                            print(438,e)
                except:
                    pass

                for i in range(grid_layout.count()):
                    try:
                        grid_layout.itemAt(i).widget().setCheckable(True)
                    except:
                        pass

                notes_box = QTextEdit(self)
                notes_box.setPlaceholderText('Notes')
                notes_box.setMaximumSize(int(self.swidth / 1.35), 100)

                quantity_box = QSpinBox()
                quantity_box.setMinimum(1)
                quantity_box.setValue(1)
                quantity_box.setAlignment(QtCore.Qt.AlignCenter)
                quantity_box.setObjectName('department-submit')

                submit_layout = QVBoxLayout()

                submit_button = QPushButton("Submit", self)
                submit_button.clicked.connect(lambda: self.submit_item())
                submit_button.setObjectName('department-submit')

                cancel_button = QPushButton("Cancel", self)
                cancel_button.clicked.connect(lambda: self.close_window())
                cancel_button.setObjectName('department-submit')

                submit_layout.addWidget(quantity_box)
                submit_layout.addWidget(cancel_button)
                submit_layout.addWidget(submit_button)

                notes_layer = QHBoxLayout()
                notes_layer.addWidget(notes_box)
                notes_layer.addLayout(submit_layout)
                # self.notes_layer.setMaximumSize(400,600)

                secondary_layout_V = QVBoxLayout()
                secondary_layout_V.addLayout(grid_layout)
                #self.secondary_layout_V.addLayout(secondary_layout_H)
                #for layer in self.extras_menus[index]:
                    #self.secondary_layout_V.addLayout(layer)
                # self.secondary_layout_V.addWidget(notes_box)
                # self.secondary_layout_V.addWidget(quantity_box)
                # self.secondary_layout_V.addLayout(submit_layout)
                secondary_layout_V.addLayout(notes_layer)

                # self.outer_layer.insertLayout(0,self.secondary_layout_V)
                # self.mini_window = Department(index)
                widget.setLayout(secondary_layout_V)
                self.department_widget.addWidget(widget)

                self.department_widgets.append(secondary_layout_V)

        except Exception as e:
            print(509,e)

    def submit_item(self):
        try:
            for index in range(self.department_grid.count()):
                if self.department_grid.itemAt(index).widget().isChecked():
                    break

            order = [department_menu[index][0], [], [], "", 0, [0, [], []]]

            grid = self.department_widgets[index].itemAt(0).layout() #the grid layout
            notes = self.department_widgets[index].itemAt(1).itemAt(0).widget()
            quantity = self.department_widgets[index].itemAt(1).itemAt(1).itemAt(0).widget()

            for row in range(grid.rowCount()):
                try:
                    #if grid.itemAtPosition(row,0).widget().text() == "Type:" or grid.itemAtPosition(row,0).widget().text() == "":
                    if grid.itemAtPosition(row,0).widget().objectName() == "flavor-menu":
                        for col in range(grid.columnCount()):
                            try:
                                if grid.itemAtPosition(row,col+1).widget().isChecked():
                                    order[1].append(grid.itemAtPosition(row,col+1).widget().text())
                                    grid.itemAtPosition(row, col + 1).widget().setChecked(False)
                            except:
                                pass
                    else: #Means Extras
                        for col in range(grid.columnCount()):
                            try:
                                if grid.itemAtPosition(row, col + 1).widget().isChecked():
                                    order[2].append(grid.itemAtPosition(row, col + 1).widget().text())
                                    grid.itemAtPosition(row, col + 1).widget().setChecked(False)
                            except:
                                pass
                except:
                    pass


            order[3] = (notes.toPlainText())
            notes.clear()

            order[4] = (int(quantity.value()))
            quantity.setValue(1)

            order[5][0] = (department_menu[index][1])  # Price of department
            for flav in order[1]:  # Price of Flavor
                for x in flavor_menu[index]:
                    if flav in x:
                        order[5][1].append(x[1])
                        break

            for ext in order[2]:  # Price of Extras
                for y in extras_menu[index]:
                    if ext in y:
                        order[5][2].append(y[1])
                        break

            cart.cart.append(order)

            # self.set_cart_text()

            self.update_cart()
            self.open_cart()

        except Exception as e:
            print(e)

    def reset(self):
        self.name_box.clear()
        # NEED TO RESET CART - Get Rid Items, Delete order number and price
        cart.reset()

        self.update_cart()
        self.department_widget.setCurrentIndex(0)
        # self.set_cart_text()

    def close_window(self):
        index = self.department_widget.currentIndex()
        self.open_cart()

    def open_cart(self):
        # self.cart = Cart_GUI()
        for i in range(self.department_grid.count()):
            self.department_grid.itemAt(i).widget().setChecked(False)
        self.department_widget.setCurrentIndex(0)

    def submit_cart(self):
        try:
            if self.name_box.text() == '':
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Warning")
                #self.msg.setIcon() TODO: set Icon for messagebox
                self.msg.setText("There is no Customer Name entered")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
                self.msg.buttonClicked.connect(self.name_popup_button)
                self.msg.exec_()
            else:
                self.submit_cart_2()
        except Exception as e:
            print(e)
    def name_popup_button(self,btn):
        try:
            if btn.text() == 'Cancel' or btn.text() == 'Retry':
                self.msg.close()
            elif btn.text() == 'Ignore':
                self.submit_cart_2()
        except Exception as e:
            print(e)
    def submit_cart_2(self): #TODO: auto move order to open spots in other windows and auto delete window if empty
        #If auto move - have to account for different numbers - just change to if see just a number??
        self.found_box = False
        first_time = True
        iter_all = False
        pointer = Pier2.main_widget.currentIndex()
        widg = pointer
        try:
            if cart.cart != []:
                widget = Pier2.main_widget.currentWidget().layout()
                for index in range(widget.count()): #Tries current window
                    #if widget.itemAt(index).widget().toPlainText() == str(index + 1+pointer*ORDER_GRID_ROW*ORDER_GRID_COL):
                        #self.put_order_into_boxes(widget,index)
                        #break
                    try: #Change to just see a number
                        int(widget.itemAt(index).widget().toPlainText())
                        self.put_order_into_boxes(widget, index)
                        break
                    except:
                        pass
                while not self.found_box:
                    for pointer in range(Pier2.main_widget.count()):
                        widget = Pier2.main_widget.widget(pointer).layout()
                        # This puts the order into the grid layout
                        for index in range(widget.count()):
                            #if widget.itemAt(index).widget().toPlainText() == str(index + 1+pointer*ORDER_GRID_ROW*ORDER_GRID_COL):
                                #self.put_order_into_boxes(widget, index)
                                #break
                            try:  # Change to just see a number
                                int(widget.itemAt(index).widget().toPlainText())
                                self.put_order_into_boxes(widget, index)
                                break
                            except:
                                pass

                        if self.found_box:
                            break

                    if not self.found_box:
                        Pier2.create_widget()

                # puts the order into excel
                pexc.submit_order_data(self.name_box.text(), cart.cart)

                self.name_box.clear()
                self.reset()
                Pier2.main_widget.setCurrentIndex(widg)

            else:
                pass

        except Exception as e:
            print(e)

    def put_order_into_boxes(self,widget,index):
        self.found_box = True

        if self.name_box.text != "":
            widget.itemAt(index).widget().append(self.name_box.text() + "\n")

        for order in cart.cart:
            flavor = ""
            for n in order[1]:
                flavor += n + ", "

            extras = ""
            for e in order[2]:
                extras += e + ", "
            widget.itemAt(index).widget().append(
                str(order[4]) + " " + order[0] + " - " + flavor)
            if extras != "":
                widget.itemAt(index).widget().append(extras)
            if order[3] != "":
                widget.itemAt(index).widget().append(order[3])
            widget.itemAt(index).widget().append("")  # "\n")

    def submit_order_2(self):
        for index in range(Pier2.number_order_boxes):
            if Pier2.order_layout.itemAt(index).widget().toPlainText() == "":
                Pier2.order_layout.itemAt(index).widget().setText(self.name_box.text()
                                                                  + "\n"
                                                                  + "\n" + self.notes_box.toPlainText())
                break
            else:
                pass
            # put into memory/excel sheet for later
            # indicate how many are out of the screen
            # CLEAR form

    def set_cart_text(self):
        summ = 0
        for it in cart.cart:
            summ += 1
        self.cart_button.setText("Cart (" + str(summ) + ")")


    def update_cart(self):
        try:
            total_price = 0
            total_items = 0
            self.main_layout = QVBoxLayout()

            label_layout = QHBoxLayout()

            item_label = QLabel("Item", self)
            item_label.setAlignment(QtCore.Qt.AlignCenter)
            item_label.setObjectName('cart-main-label')
            # item_label.setStyleSheet("border :5px solid ;"
            # "border-bottom-color : black")
            # "border-top-color : red; "
            # "border-left-color : black; "
            # "border-right-color : black; "
            # "border-bottom-color : green")

            quantity_label = QLabel("Quantity", self)
            quantity_label.setAlignment(QtCore.Qt.AlignCenter)
            quantity_label.setObjectName('cart-quantity')
            #quantity_label.setMinimumWidth() SAME AS Pushbutton
            # TODO: Change cart to Grid?

            price_label = QLabel("Price", self)
            price_label.setAlignment(QtCore.Qt.AlignCenter)
            price_label.setObjectName('cart-main-label')
            # price_label.setFont(QFont("Sanserif", 14))

            align_label = QLabel("")
            align_label.setObjectName('cart-align')
            #align_labe.setMaximumWidth() SAME AS DELETE BUTTONS

            label_layout.addWidget(item_label)
            label_layout.addWidget(quantity_label)
            label_layout.addWidget(price_label)
            label_layout.addWidget(align_label)
            self.main_layout.addLayout(label_layout)

            self.delete_buttons = []
            self.menu_list = []
            for order in cart.cart:
                gen_layout = QHBoxLayout()

                flav_name = ""
                for n in order[1]:
                    if flav_name == "":
                        flav_name += n
                    else:
                        flav_name += ", " + n
                extras = ""
                for e in order[2]:
                    if extras == "":
                        extras += e
                    else:
                        extras += ", " + e
                name = order[0] + " (" + flav_name + ")"
                name_box = QLabel()
                name_box.setWordWrap(True)
                name_box.setText(name + "\n" + extras + "\n" + order[3])
                name_box.setAlignment(QtCore.Qt.AlignCenter)
                name_box.setTextFormat(QtCore.Qt.RichText)
                name_box.setObjectName('cart-item')
                # TODO: add what extra charges for

                price = 0
                for p in order[5]:
                    if type(p) == list:
                        for x in p:
                            price += x
                    else:
                        price += p
                price *= order[4]
                price_box = QLabel("$" + str(price))
                price_box.setAlignment(QtCore.Qt.AlignCenter)

                #quantity_box = QLabel(str(order[4]))
                #quantity_box.setAlignment(QtCore.Qt.AlignCenter)
                quantity_box = QPushButton(str(order[4]))
                quantity_box.setObjectName('cart-button')
                #quantity_box.setMaximumSize(100,40)
                #quantity_box.setStyleSheet("border : 2px solid black; border-radius : 20px;")
                #quantity_box.setMaximumSize(200,50)
                menu_options = ['1','2','3','4','5','6','7','8','9','10']
                menu = QMenu()
                menu.triggered.connect(lambda x: self.update_cart_quantity(x.text()))
                for num in menu_options:
                    menu.addAction(num)
                quantity_box.setMenu(menu)
                self.menu_list.append(menu)


                delete_box = QPushButton("Delete")
                delete_box.clicked.connect(lambda: self.delete_order())
                delete_box.setObjectName('cart-button')
                #delete_box.setMaximumWidth()

                gen_layout.addWidget(name_box)
                gen_layout.addWidget(quantity_box)
                gen_layout.addWidget(price_box)
                gen_layout.addWidget(delete_box)

                self.main_layout.addLayout(gen_layout)

                self.delete_buttons.append(gen_layout)

                total_price += price * order[4]
                total_items += order[4]

            total_layout = QHBoxLayout()

            total_label = QLabel("Total")
            total_label.setAlignment(QtCore.Qt.AlignCenter)
            total_label.setObjectName('cart-total')

            total_items_label = QLabel(str(total_items))
            total_items_label.setAlignment(QtCore.Qt.AlignCenter)
            total_items_label.setObjectName('cart-total-quantity')
            #total_items_label.setMinimumWidth() SAME AS Pushbutton

            total_price_label = QLabel("$"+str(total_price))
            total_price_label.setAlignment(QtCore.Qt.AlignCenter)
            total_price_label.setObjectName('cart-total-price')

            total_layout.addWidget(total_label)
            total_layout.addWidget(total_items_label)
            total_layout.addWidget(total_price_label)
            total_layout.addWidget(align_label)

            self.main_layout.addLayout(total_layout)

            # cancel/submit buttons
            submit_layout = QHBoxLayout()
            submit_button = QPushButton("Submit Order", self)
            submit_button.clicked.connect(lambda: self.submit_cart())
            submit_button.setObjectName('cart-submit')
            close_button = QPushButton("Cancel Order", self)
            close_button.clicked.connect(lambda: self.reset())
            close_button.setObjectName('cart-submit')
            submit_layout.addWidget(close_button)
            submit_layout.addWidget(submit_button)
            self.main_layout.addLayout(submit_layout)

            self.department_widget.removeWidget(self.cart_widget)

            self.cart_widget = QWidget()
            self.cart_widget.setLayout(self.main_layout)
            self.department_widget.insertWidget(0, self.cart_widget)
            self.department_widget.update()
            self.department_widget.setCurrentIndex(0)


        except Exception as e:
            print(e)

    def update_cart_quantity(self,quantity):
        try:
            btn = self.sender()

            index = 0
            for menu in self.menu_list:
                if btn == menu:
                    break
                index += 1

            cart.cart[index][4] = int(quantity)
            self.update_cart()
        except Exception as e:
            print(e)

    def delete_order(self):
        try:
            button = self.sender()

            # have to iterate through each layer to see which one the button came from
            pointer = 0
            for layer in self.delete_buttons:
                index = layer.indexOf(button)
                if index != -1:
                    break
                pointer += 1

            cart.cart.pop(pointer)

            self.update_cart()


        except Exception as e:
            print(e)
        pass

class Order_Tab(QWidget):
    def __init__(self):
        super().__init__()

        self.styleSheet = f'''
        
        QPushButton#grid-layout{{
            background-color: rgba(75,133,180,0.2);
            border-style: outset;
            border-width: 1px;
            border-radius: 10px;
            border-color: grey;
            padding: 0px;
            font: bold 12px;
            max-height: {25}px;
            min-height: {25}px;
            max-width: 300px;
        }}
        QPushButton#grid-layout:pressed{{
            color: white;
            background-color: rgba(20,100,20,.4);
            border-color: grey;
        }}
        
        QToolButton{{
            background-color: rgba(205,205,205,1);
            min-height: 40px;
            min-width: 40px;
        }}
        
        QLabel#order-label{{
            font: bold 14px;
            max-width: 200px;
        }}
        
        QRadioButton{{
            font: bold 12px;
            max-width: 150px;
        }}
        
        '''

        self.setStyleSheet(self.styleSheet)

        self.UIComponents()

    def UIComponents(self): #TODO: Create Scrolling Button? or just make windows smaller, or if too large, put to new window
        # TODO: subparts of order completed button???
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(100)

        self.order_fwd_btn = QToolButton()
        self.order_fwd_btn.setArrowType(QtCore.Qt.RightArrow)
        self.order_back_btn = QToolButton()
        self.order_back_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.order_fwd_btn.clicked.connect(self.order_move)
        self.order_back_btn.clicked.connect(self.order_move)

        self.order_label = QLabel("Switch Order Screens:")
        #self.order_label.setAlignment(QtCore.Qt.AlignLeft)
        self.order_label.setObjectName("order-label")

        self.order_btn_layout = QHBoxLayout()
        self.order_btn_layout.addWidget(self.order_back_btn)
        self.order_btn_layout.addWidget(self.order_fwd_btn)
        #self.order_btn_layout = QHBoxLayout()
        #self.order_btn_layout.setSpacing(20)
        #self.order_btn_layout.addWidget(self.order_label)
        #self.order_btn_layout.addWidget(self.order_back_btn)
        #self.order_btn_layout.addWidget(self.order_fwd_btn)

        #self.order_status_layer = QHBoxLayout()
        #self.order_status_layer.setSpacing(20)
        self.working_status_btn = QRadioButton("Started",self)
        self.completed_status_btn = QRadioButton("Completed",self)
        self.stopped_btn = QRadioButton("Stopped")
        #self.order_status_layer.addWidget(self.working_status_btn, alignment=QtCore.Qt.AlignCenter)
        #self.order_status_layer.addWidget(self.completed_status_btn, alignment=QtCore.Qt.AlignCenter)

        self.grid_layout.addWidget(self.order_label,0,0)
        self.grid_layout.addLayout(self.order_btn_layout,0,1)
        self.grid_layout.addWidget(self.stopped_btn,1,0)
        self.grid_layout.addWidget(self.working_status_btn,1,1)
        self.grid_layout.addWidget(self.completed_status_btn, 1, 2)

        self.group = QButtonGroup()
        self.group.addButton(self.working_status_btn)
        self.group.addButton(self.completed_status_btn)
        self.group.addButton(self.stopped_btn)

        # Completed Order Grid
        self.completed_orders_grid = QGridLayout()

        for i in range(0, ORDER_GRID_ROW):
            for j in range(0, ORDER_GRID_COL):
                self.completed_orders_grid.addWidget(QPushButton(str((i) * (ORDER_GRID_COL) + (j + 1)), self), i, j)
        for i in range(self.completed_orders_grid.count()):
            self.completed_orders_grid.itemAt(i).widget().clicked.connect(lambda: self.set_order_boxes())
            self.completed_orders_grid.itemAt(i).widget().setObjectName('grid-layout')

        self.outer_layer = QVBoxLayout()
        #self.outer_layer.addLayout(self.order_btn_layout)
        #self.outer_layer.addLayout(self.order_status_layer)
        self.outer_layer.addLayout(self.grid_layout)
        self.outer_layer.addLayout(self.completed_orders_grid)

        self.setLayout(self.outer_layer)

    def set_order_boxes(self):
        try:
            button = self.sender()
            index = self.completed_orders_grid.indexOf(button)
            if self.working_status_btn.isChecked():
                Pier2.main_widget.currentWidget().layout().itemAt(index).widget().setStyleSheet("background: rgb(0,128,0,0.6)")
            elif self.completed_status_btn.isChecked():
                Pier2.main_widget.currentWidget().layout().itemAt(index).widget().clear()
                Pier2.main_widget.currentWidget().layout().itemAt(index).widget().setStyleSheet("background: rgb(255,255,255,1)")
                Pier2.main_widget.currentWidget().layout().itemAt(index).widget().setText(str(index + 1 +
                                                    Pier2.main_widget.currentIndex()*ORDER_GRID_COL*ORDER_GRID_ROW))
            elif self.stopped_btn.isChecked():
                Pier2.main_widget.currentWidget().layout().itemAt(index).widget().setStyleSheet("background: white")

            self.group.setExclusive(False)
            self.working_status_btn.setChecked(False)
            self.completed_status_btn.setChecked(False)
            self.stopped_btn.setChecked(False)
            self.group.setExclusive(True)
        except Exception as e:
            print(e)

    def order_move(self):
        btn = self.sender()
        index = Pier2.main_widget.currentIndex()
        try:
            if btn == self.order_fwd_btn:
                Pier2.main_widget.setCurrentIndex(index+1)
            elif btn == self.order_back_btn:
                Pier2.main_widget.setCurrentIndex(index-1)
        except Exception as e:
            print(e)


class Cart():
    def __init__(self):
        super().__init__()
        self.cart = []

    def reset(self):
        self.cart = []


class Orders(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pier 142 Orders")

        # CHange for WHEN HAVE MULTIPLE SCREENS??
        self.screen = app.primaryScreen()
        self.swidth = self.screen.size().width()
        self.sheight = self.screen.size().height()

        # see how many order boxes can fit in screen
        self.number_order_boxes_height = int(self.sheight / order_height)
        self.number_order_boxes_width = int(self.swidth / order_width)

        self.UIComponents()
        self.showMaximized()

    def UIComponents(self):
        # Order Boxes
        # self.notes_box = QTextEdit(self)
        # self.notes_box.setGeometry(self.Qcenter,250,Qheight,200)
        # self.notes_box.setPlaceholderText('Notes')
        self.main_widget = QStackedWidget()

        self.order_layout = QGridLayout()

        # Create Grid Layout of order boxes
        # CHANGE NUMBERS TO FIT SCREEN SIZE!!!)
        for i in range(0, ORDER_GRID_ROW):
            for j in range(0, ORDER_GRID_COL):
                self.order_layout.addWidget(QTextEdit(self), i, j)

        #self.setLayout(self.order_layout)

        self.number_order_boxes = self.order_layout.count()

        for index in range(self.number_order_boxes):
            self.order_layout.itemAt(index).widget().setStyleSheet("fontName='Times'")
            self.order_layout.itemAt(index).widget().setFont(QFont('Time font', 12))
            self.order_layout.itemAt(index).widget().setText(str(index + 1))
            # self.order_layout.itemAt(index).widget().setStyleSheet("background: rgb(0,128,0,0.6)")

        widget = QWidget()
        widget.setLayout(self.order_layout)
        self.main_widget.addWidget(widget)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)

    def create_widget(self):
        order_layout = QGridLayout()

        # Create Grid Layout of order boxes
        # CHANGE NUMBERS TO FIT SCREEN SIZE!!!)
        for i in range(0, ORDER_GRID_ROW):
            for j in range(0, ORDER_GRID_COL):
                order_layout.addWidget(QTextEdit(self), i, j)

        # self.setLayout(self.order_layout)

        number_order_boxes = order_layout.count()
        total_num = self.main_widget.count()

        for index in range(number_order_boxes):
            order_layout.itemAt(index).widget().setStyleSheet("fontName='Times'")
            order_layout.itemAt(index).widget().setFont(QFont('Time font', 12))
            order_layout.itemAt(index).widget().setText(str(index + 1+total_num*ORDER_GRID_ROW*ORDER_GRID_COL))
            # self.order_layout.itemAt(index).widget().setStyleSheet("background: rgb(0,128,0,0.6)")

        widget = QWidget()
        widget.setLayout(order_layout)
        self.main_widget.addWidget(widget)
        #index = self.main_widget.currentIndex()
        self.main_widget.setCurrentIndex(self.main_widget.indexOf(widget))
        #return index


class Change_Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.styleSheet = '''
            QPushButton#change-btn{
                background-color: rgba(205,205,205);
                font: bold 12px;
                border: 1px solid black;
                border-radius: 10px;
                max-width: 400px;
                min-height: 30px;
            }
            QPushButton#change-btn:pressed{
                background-color: grey;
            }
            QCheckBox{
                font: bold 12px;
                max-width: 200px;
            }
            QRadioButton{
                font: bold 12px;
                min-width: 100px;
            }
            
            QLabel#header{
                font: bold 14px;
                max-height: 30px;
            }
            QLabel#add{
                font: bold 12px;
                max-width: 300px;
                max-height: 30px;
            }
            QLineEdit#add{
                max-height: 30px;
            }
            QLineEdit#add2{
                max-height: 30px;
                max-width: 250px;
            }
            QPushButton#add-btn{
                background-color: rgba(205,205,205);
                font: bold 12px;
                border: 1px solid black;
                border-radius: 10px;
                max-width: 400px;
                min-height: 30px;
            }
            QPushButton#add-btn:pressed{
                background-color: grey;
            }
        '''
        self.setStyleSheet(self.styleSheet)

        self.UIComponents()

    def UIComponents(self):

        self.stacked_widget = QStackedWidget()
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.stacked_widget)

        main_dep_lay = QVBoxLayout()
        dep_layout = QHBoxLayout()
        dep_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.dep_btns = []
        self.dep_group = QButtonGroup()
        for dep in department_menu:
            btn = QRadioButton(dep[0])
            dep_layout.addWidget(btn)
            self.dep_btns.append(btn)
            self.dep_group.addButton(btn)

        widget1 = QWidget()
        widget1.setLayout(main_dep_lay)
        self.stacked_widget.addWidget(widget1)

        self.add_btn = QPushButton("Add Menu")
        self.add_btn.clicked.connect(self.add_menu_widget)
        self.edit_btn = QPushButton("Edit")
        self.edit_btn.clicked.connect(self.edit_menu_widget)
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.menu_delete_btn)
        self.permanent_btn = QCheckBox("Permanent")

        self.btn_layout = QHBoxLayout()
        for btn in (self.add_btn, self.edit_btn, self.delete_btn):  # ,self.permanent_btn):
            btn.setObjectName("change-btn")
            self.btn_layout.addWidget(btn)
            # btn.clicked.connect(self.menu_popup_btn)
        self.btn_layout.addWidget(self.permanent_btn)

        main_dep_lay.addLayout(dep_layout)
        main_dep_lay.addLayout(self.btn_layout)

        self.setLayout(self.main_layout)

    def btns_checked(self):
        dep = None
        for btn in self.dep_btns:
            if btn.isChecked():
                dep = btn.text()
        if dep is None:
            msg = QMessageBox()
            msg.setWindowTitle("No Button Selected")
            msg.setText("Please select a menu item")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return False
        else:
            return True

    def add_menu_widget(self):
        self.isEdit = False
        add_main_layout = QVBoxLayout()
        add_main_layout.addWidget(QLabel("Add item and price as comma separated list (extra1,price1,extra2,price2)"))
        add_main_layout.itemAt(0).widget().setObjectName("header")
        add_main_layout.itemAt(0).widget().setAlignment(QtCore.Qt.AlignCenter)

        self.add_grid = QGridLayout()
        self.add_grid.addWidget(QLabel("Item Name and Price:"),0,0)
        self.add_grid.addWidget(QLineEdit(),0,1)
        self.add_grid.addWidget(QLabel("Item Types Label:"),1,0)
        self.add_grid.addWidget(QLineEdit(),1,1)
        self.add_grid.addWidget(QLabel("Item Types and Prices:"),1,2)
        self.add_grid.addWidget(QLineEdit(),1,3)
        self.add_grid.addWidget(QLabel("Item Extras Label:"),2,0)
        self.add_grid.addWidget(QLineEdit(),2,1)
        self.add_grid.addWidget(QLabel("Item Extras and Prices:"),2,2)
        self.add_grid.addWidget(QLineEdit(),2,3)
        self.add_row = 3

        self.add_btn = QPushButton("Add Extras")
        self.add_btn.clicked.connect(self.add_extra)
        self.add_grid.addWidget(self.add_btn,3,0)

        for i in range(self.add_grid.count()):
            if (i+1)%4 == 0 or i == 1:
                self.add_grid.itemAt(i).widget().setObjectName("add2")
            else:
                self.add_grid.itemAt(i).widget().setObjectName("add")

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.zero)
        add_btn = QPushButton("Done")
        add_btn.clicked.connect(self.change_menu1)
        self.add_permanent = QCheckBox("Permanent")
        btn_layout = QHBoxLayout()
        for btn in (back_btn,add_btn,self.add_permanent):
            btn_layout.addWidget(btn)
            btn.setObjectName("add-btn")
        add_main_layout.addLayout(self.add_grid)
        add_main_layout.addLayout(btn_layout)


        widget = QWidget()
        widget.setLayout(add_main_layout)
        self.stacked_widget.addWidget(widget)

        self.add_widget_index = self.stacked_widget.currentIndex()+1
        self.stacked_widget.setCurrentIndex(self.add_widget_index)

    def add_extra(self):
        self.add_grid.removeWidget(self.add_btn)
        self.add_grid.addWidget(QLabel("Item Extras Label:"), self.add_row, 0)
        self.add_grid.addWidget(QLineEdit(), self.add_row, 1)
        self.add_grid.addWidget(QLabel("Item Extras and Prices:"), self.add_row, 2)
        self.add_grid.addWidget(QLineEdit(), self.add_row, 3)

        self.add_row += 1
        self.add_grid.addWidget(self.add_btn,self.add_row,0)

        for i in range(self.add_grid.count()):
            if (i + 1) % 4 == 0 or i == 1:
                self.add_grid.itemAt(i).widget().setObjectName("add2")
            else:
                self.add_grid.itemAt(i).widget().setObjectName("add")

    def edit_menu_widget(self):
        try:
            if self.btns_checked():
                self.add_menu_widget()
                self.isEdit = True

                for btn in self.dep_btns:
                    if btn.isChecked():
                        dep = btn.text()
                for menu in department_menu:
                    for item in menu:
                        if item == dep:
                            index = department_menu.index(menu)
                self.add_grid.itemAt(1).widget().setText(department_menu[index][0]+","+str(department_menu[index][1]))
                self.add_grid.itemAt(3).widget().setText(label_menu[index][0].replace(":",''))

                text = ''
                i=0
                for flav in flavor_menu[index]:
                    text += flav[0]+","+str(flav[1])
                    if i < len(flavor_menu[index])-1:
                        text += ","
                    i+=1
                self.add_grid.itemAt(5).widget().setText(text)

                lab_ind = 1
                row = 9
                for ext1 in extras_menu[index]:
                    if row > 9:
                        self.add_extra()
                    self.add_grid.itemAt(row-2).widget().setText(label_menu[index][lab_ind].replace(":",''))
                    text = ''
                    i=0
                    for ext2 in ext1:
                        text += ext2[0]+","+str(ext2[1])
                        if i < len(ext1) - 1:
                            text += ","
                        i += 1
                    self.add_grid.itemAt(row).widget().setText(text)
                    row+=4
                    lab_ind += 1

        except Exception as e:
            print(e)

    def zero(self):
        self.stacked_widget.removeWidget(self.stacked_widget.widget(self.stacked_widget.currentIndex()))
        self.stacked_widget.setCurrentIndex(0)
        #for btn in self.dep_btns: Unselect button
            #btn.setChecked(True)

    def change_menu1(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Warning")
        # self.msg.setIcon() TODO: set Icon for messagebox
        if self.add_permanent.isChecked():
            self.msg.setText("Are you sure you want to <b>permanently</b> change the menu?")
        else:
            self.msg.setText("Are you sure you want to change the menu?")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
        self.msg.buttonClicked.connect(self.check_change_msg)
        self.msg.exec_()

    def check_change_msg(self,btn):
        if btn.text() == "&Yes":
            self.change_menu()
        else:
            self.msg.close()
        self.add_permanent.setChecked(False)

    def change_menu(self): #TODO: add warning for if no label/extra but the other is present?
        try:
            department = self.add_grid.itemAt(1).widget().text()
            if department == "":
                raise ValueError("No Item Name")
            department = department.replace(", ",",")

            flavor_label = self.add_grid.itemAt(3).widget().text() + ":"
            flavor = self.add_grid.itemAt(5).widget().text()
            flavor = flavor.replace(", ",",")
            if flavor_label == ":":
                raise ValueError("No Flavor Label")
            if flavor == "":
                raise ValueError("No Flavors")

            extras = []
            extra_labels = []
            for i in range(7,self.add_grid.count()-1):
                x=self.add_grid.getItemPosition(i)[1]
                text = self.add_grid.itemAt(i).widget().text()
                if text == "":
                    pass
                if x == 1:
                    extra_labels.append(text + ":")
                elif x == 3:
                    extras.append(text)

            if self.add_permanent.isChecked(): #TODO: Not Storing in excel correctly
                sheet = pexc.wb["Menu"]
                START_ROW = 2
                row = START_ROW
                col = 67
                if self.isEdit:
                    for btn in self.dep_btns:
                        if btn.isChecked():
                            dep = btn.text()
                    for menu in department_menu:
                        for item in menu:
                            if item == dep:
                                index = department_menu.index(menu)
                    row = index+START_ROW
                else:
                    value = sheet["A"+str(row)].value
                    while value is not None or value != "":
                        row += 1
                        value = sheet["A" + str(row)].value
                sheet["A"+str(row)] = department
                sheet["B"+str(row)] = flavor_label + flavor
                for index in range(len(extras)):
                    sheet[chr(col)+str(row)] = extra_labels[index]+extras[index]
                    col+=1
                pexc.wb.save(pexc.file)

            labels = extra_labels
            labels.insert(0,flavor_label)
            depart = self.read_cell(department)
            if not len(depart) == 2:
                raise ValueError("No Item name or price")
            dep = [depart[0],int(depart[1])]

            flav = []
            flavors = self.read_cell(flavor)
            i = 0
            while i < len(flavors):
                try:
                    flav.append([flavors[i], int(flavors[i + 1])])
                    i += 2
                except:
                    flav.append([flavors[i], 0])
                    i += 1
            extra = []
            for ext in extras:
                extra.append(self.read_cell(ext))

            extra1 = []
            index = 0
            for ext in extra:
                extra1.append([])
                i = 0
                while i < len(ext):
                    try:
                        extra1[index].append([ext[i], int(ext[i + 1])])
                        i += 2
                    except:
                        extra1[index].append([ext[i], 0])
                        i += 1
                index+=1

            if self.isEdit:
                index = self.delete(refresh = False)
                department_menu.insert(index,dep)
                flavor_menu.insert(index,flav)
                extras_menu.insert(index,extra1)
                label_menu.insert(index,labels)
            else:
                department_menu.append(dep)
                flavor_menu.append(flav)
                extras_menu.append(extra1)
                label_menu.append(labels)

            self.refresh()
        except ValueError as er:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            # self.msg.setIcon() TODO: set Icon for messagebox
            msg.setText(str(er))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except Exception as e:
            log_error(sys.exc_info())

    def read_cell(self,string):
        text = ''
        words = []
        for let in string:
            if let == ',':
                if text != '':
                    words.append(text)
                    text = ''
            else:
                text += let
        if text != '':
            words.append(text)
        return words


    def menu_delete_btn(self):
        if self.btns_checked():
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Warning")
            # self.msg.setIcon() TODO: set Icon for messagebox
            if self.permanent_btn.isChecked():
                self.msg.setText("Are you sure you want to <b>permanently</b> delete this item?")
            else:
                self.msg.setText("Are you sure you want to delete this item?")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
            self.msg.buttonClicked.connect(self.check_delete_msg)
            self.msg.exec_()

    def check_delete_msg(self, btn):
        if btn.text() == "&Yes" and self.permanent_btn.isChecked():
            self.delete_permanent()
        if btn.text() == "&Yes" and not self.permanent_btn.isChecked():
            self.delete()
        self.msg.close()
        self.permanent_btn.setChecked(False)

    def delete_permanent(self):
        index = self.delete()
        sheet = pexc.wb["Menu"]
        START_ROW = 2
        row = START_ROW + index
        #col = 66
        #value = sheet["A" + str(row)].value
        #while value is not None or value != "":
            #sheet[chr(col) + str(row)].value = None
        sheet.delete_rows(row,1)
        pexc.wb.save(pexc.file)

    def delete(self,refresh = True):
        try:
            for btn in self.dep_btns:
                if btn.isChecked():
                    dep = btn.text()
            for menu in department_menu:
                for item in menu:
                    if item == dep:
                        index = department_menu.index(menu)
            department_menu.pop(index)
            flavor_menu.pop(index)
            extras_menu.pop(index)
            label_menu.pop(index)

            if refresh:
                self.refresh()
            return index
        except Exception as e:
            print(e)

    def refresh(self):
        index = main_window.tabs.currentIndex()
        main_window.tabs.removeTab(0)
        main_window.tabs.insertTab(0,Register(),"Register")
        main_window.tabs.removeTab(3)
        main_window.tabs.insertTab(3,Change_Menu(),"Change Menu")
        main_window.tabs.setCurrentIndex(index)

class Tabs(QMainWindow):
    def __init__(self):
        super().__init__()

        self.styleSheet = f"""
        
        QTabBar::tab{{
            font: bold 12px;
            width: 150px;
            background: rgba(20,80,100,0.2);
        }}
        QTabBar::tab:selected{{
            background-color: rgba(202,241,222,0.4);
        }}
        QTabWidget>QWidget>QWidget{{
            background: white;
        }}
        
        #QMainWindow{{
            background-color: grey;
        }}
        
        """
        self.setStyleSheet(self.styleSheet)

        # self.Pier1 = Register()
        self.tabs = QTabWidget()
        self.register_tab = Register()
        self.order_tab = Order_Tab()
        self.menu_tab = Change_Menu()
        self.stats_tab = pexc.Sales()

        # self.register_tab.setLayout(self.Pier1.outer_layer)
        self.menu_tab.setLayout(QVBoxLayout())
        self.stats_tab.setLayout(QHBoxLayout())

        self.tabs.addTab(self.register_tab, "Register")
        self.tabs.addTab(self.order_tab, "Orders")
        self.tabs.addTab(self.stats_tab, "Stats")
        self.tabs.addTab(self.menu_tab, "Change Menu")

        self.setCentralWidget(self.tabs)
        self.setWindowTitle("Pier 142")

        self.showMaximized()

def get_menu_lists():
    global department_menu
    global flavor_menu
    global extras_menu
    global label_menu
    department_menu = pexc.department_menu
    flavor_menu = pexc.flavor_menu
    extras_menu = pexc.extras_menu
    label_menu = pexc.label_menu

def log_error(info):
    try:
        traceback_template = '''File "%(filename)s", line %(lineno)s, in %(name)s
        %(type)s: %(message)s\n'''

        exc_type, exc_value, exc_traceback = info

        traceback_details = {
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'lineno': exc_traceback.tb_lineno,
            'name': exc_traceback.tb_frame.f_code.co_name,
            'type': exc_type.__name__,
        }

        del (exc_type, exc_value, exc_traceback)

        #print (traceback.format_exc())
        #print (traceback_template % traceback_details)
        #print (info[0].__name__,os.path.basename(info[2].tb_frame.f_code.co_filename), info[2].tb_lineno)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    cart = Cart()
    # Pier1 = Register()
    pexc.get_menu()
    get_menu_lists()
    Pier2 = Orders()
    main_window = Tabs()
    sys.exit(app.exec_())

    #monitor = QDesktopWidget().screenGeometry(2) #TODO: make go to Monitor
    #Pier2.move(monitor.left(),monitor.top())
    #Pier2.showFullScreen()
    #Pier2.activateWindow() Brings to Front


