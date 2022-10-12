import matplotlib.pyplot as plt

COLOR_MAP = 'YlGnBu'

def display_images(images: list):
    fig, axs = plt.subplots(1, len(images), figsize=(12, 12))
    for i in range(len(images)):
        axs[i].axis('off')
        axs[i].imshow(images[i], cmap=COLOR_MAP)
        axs[i].title.set_text(f"Image {i+1}")
        for j in range(images[i].shape[0]):
            for k in range(images[i].shape[1]):
                axs[i].text(k, j, f"{images[i][j,k]:.2f}", fontsize="small", ha="center", va="center")
    
    plt.show()