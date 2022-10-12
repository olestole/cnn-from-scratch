import matplotlib.pyplot as plt

COLOR_MAP = 'YlGnBu'

def display_images(images, figsize=(12, 12)):
    fig, axs = plt.subplots(1, len(images), figsize=figsize)
    for i in range(len(images)):
        axs = [axs] if len(images) == 1 else axs
        axs[i].axis('off')
        axs[i].imshow(images[i][0], cmap=COLOR_MAP)
        axs[i].title.set_text(images[i][1])
        for j in range(images[i][0].shape[0]):
            for k in range(images[i][0].shape[1]):
                axs[i].text(k, j, f"{images[i][0][j,k]:.2f}", fontsize="small", ha="center", va="center")
    
    plt.show()