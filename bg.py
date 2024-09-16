from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from rembg import remove
import io
import tkinter.messagebox as tmsg
root =Tk()
root.title("BG Remover")
root.geometry("400x400")

def instruction():
     tmsg.showinfo("Instructions","""Dear user !!
                   --> This is application has very simple GUI
                   --> Choose an Image file 
                   --> Wait a while to process
                   --> save the image wat the directory
                   --> Boom its done ..""")
def messagebox():
    tmsg.showinfo("Help", "Records will update shortly!!\nPlease wait, the app is under construction")

def helpbox():
    tmsg.showinfo("Help", "Mubashir Abbas's team will help you\nPlease Contact: 03041654629")

def email():
    tmsg.showinfo("Gmail", "Please send us mail at: mubashirabbasedu12@gmail.com")
def rateus():
     tmsg.showinfo("Rate us","""Just Do a mail at mubashirabbasedu12@gmail.com you can rate us in stars as 
                   *****= Amazing
                   ****=Fair enough
                   ***=need Improvements
                   *=need improvments""")


def set_icon():
    ico = Image.open('images.jpeg')  
    photo = ImageTk.PhotoImage(ico)
    root.iconphoto(False, photo)

def openmedia():
    
    def open_image():
            image_path = filedialog.askopenfilename(
                title="Select an image",
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
            )
            return image_path
        

    def save_image(output_data):
        
            save_path = filedialog.asksaveasfilename(
                title="Save image",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if save_path:
                with open(save_path, "wb") as out_file:
                    out_file.write(output_data)
                print(f"Image saved as '{save_path}'")
            else:
                print("Save operation canceled.")

    def remove_bg(image_path):
        try:
            with open(image_path, 'rb') as img_file:
                input_image = img_file.read()
                output_image = remove(input_image)  
                save_image(output_image)
        except Exception as e:
            print(f"Error removing background: {e}")

    # Main script
    image_path = open_image()
    if image_path:
        remove_bg(image_path)
    else:
        print("No image selected.")

# Add image label
image_label = Label(root)
image_label.pack(pady=10)

# Load the image
image_path = 'images.jpeg'  
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label.config(image=photo)
image_label.image = photo  

# Add welcome label and button
Label(root, text="Welcome to BG Remover", font=("Playfair", 15, "bold"), fg="black", bg="white").pack(pady=10)
Label(root, text="Click 'open an image button' ", font=("Playfair", 10), fg="black", bg="white").pack(pady=11)
ttk.Button(root, text="Open an image", command=openmedia).pack(pady=10)
Label(root,text="© Application Developed By Mubashir Abbas ",font=("playfair",10),fg="white",bg="black").pack(pady=15)
set_icon()


mainmenu = Menu(root)

# File menu
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="How To use Application ", command=instruction)
m1.add_command(label="Help", command=helpbox)
m1.add_command(label="Rate us ", command=rateus)
m1.add_command(label="Contacts", command=email)
mainmenu.add_cascade(label="Menu", menu=m1)
root.config(menu=mainmenu)
root.mainloop()