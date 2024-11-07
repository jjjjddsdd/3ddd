import sys

from PIL import Image, ImageOps



def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_path=sys.argv[1]
    output_path=sys.argv[2]

    if input_path.split('.')[-1].lower() != output_path.split('.')[-1].lower():
        sys.exit("Input and output have different extensions")

    if not (input_path.lower().endswith(('.jpg', '.jpeg', '.png')) and output_path.lower().endswith(('.jpg', '.jpeg', '.png'))) :
        sys.exit("Input and output must be .jpg, .jpeg, or .png")

    try:
        input_image=Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_img=Image.open("shirt.png")
    input_image=ImageOps.fit(input_image, shirt_img.size, bleed=0.0)
    input_image.paste(shirt_img, (0,0), shirt_img)
    input_image.save(output_path)
    print(f"Saved output to {output_path}")

if __name__=="main":
    main()