from PIL import Image

image=Image.open("C:\\Users\\vaath\\OneDrive\\Desktop\\MY FILES\\C O D E S\\FINAL_PORTFOLIO\\PROFILE_PIC.jpg")

resized_image=image.resize((300,300))

resized_image.save("profile.jpg")

print("image resized")