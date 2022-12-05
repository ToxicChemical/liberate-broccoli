def gystfile(df):
    with(open('tablefile', 'w') as f):
        for i in df.columns:
            for j in df[i].tolist():
                print(str(j), file=f)

def Gysto(n_bins):
    # Creating dataset
    N_points = 1000

    # Creating distribution
    data = pd.read_excel("distribution" + ".xlsx")
    gystfile(data)
    with(open('tablefile', 'r') as f):
       z = list(map(float, f.readlines()))
    x = z
    y = np.random.randn(N_points)
    legend = ['distribution']

    # Creating histogram
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        axs.spines[s].set_visible(False)

    # Remove x, y ticks
    axs.xaxis.set_ticks_position('none')
    axs.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    axs.xaxis.set_tick_params(pad=5)
    axs.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    axs.grid(b=True, color='grey',
             linestyle='-.', linewidth=0.5,
             alpha=0.6)

    # Add Text watermark
    fig.text(0.9, 0.15, 'Jeeteshgavande30',
             fontsize=12,
             color='red',
             ha='right',
             va='bottom',
             alpha=0.7)

    # Creating histogram
    N, bins, patches = axs.hist(x, bins=n_bins)

    # Setting color
    fracs = ((N ** (1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # Adding extra features
    plt.xlabel("X-axis")
    plt.ylabel("y-axis")
    plt.legend(legend)
    plt.title('Customized histogram')

    # Show plot
    plt.show()
