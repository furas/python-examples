from pylab import figure, show, np
from matplotlib.widgets import MultiCursor

class MyCursor(MultiCursor):
    
    def __init__(self, *args, **kwargs):
        super(MyCursor, self).__init__(*args, **kwargs)

        # create annotations
        self.annotations = []
        
        for ax in self.axes:
            annotation = self.setup_annotation(ax, (-20,20))    
            self.annotations.append(annotation)

    def onmove(self, event):
        
        # check if mouse over any plot
        if event.inaxes: 
            # get mouse position 
            x, y = event.xdata, event.ydata
            
            # find nearest point on active plot
            idx = None
            for n, ax in enumerate(self.axes):
                if ax == event.inaxes: # find ative plot
                    idx = self.find_nearest(ax, x, y)
                    break
                        
            # change annotation on all plots
            if idx is not None: # idx can be 0 so here can't be only `if idx:`
                self.change_annotations(idx)
        else:
            self.hide_annotations()
            
        # refresh plots
        self.canvas.draw()

    def setup_annotation(self, ax, offsets):
        annotation = ax.annotate(
            '', xy=(0, 0), ha='right', xytext=offsets, 
            textcoords='offset points', va='bottom',
            bbox = dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.75),
            arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=0')
        )
            
        return annotation

    def find_nearest(self, ax, x, y):
        xdata = ax.get_lines()[0].get_xdata()
        ydata = ax.get_lines()[0].get_ydata()
        
        # find nearest point and its index
        min_dist = None
        min_idx = None
        
        for idx,(px, py) in enumerate(zip(xdata, ydata)):
            # distance without sqrt()
            dist = (px-x)**2 + (py-y)**2
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_idx = idx
        
        return min_idx

    def change_annotations(self, idx):
        # repeat for every plot
        for ann, ax in zip(self.annotations, self.axes):
            ann.set_visible(True)
            
            # get all data for this plot
            xdata = ax.get_lines()[0].get_xdata()
            ydata = ax.get_lines()[0].get_ydata()
            
            # check if idx still in this data
            if idx < len(xdata) and idx < len(ydata):
                # get position of nearest point
                x = xdata[idx]
                y = ydata[idx]
                # set annotation position and text
                ann.xy = (x, y)
                ann.set_text("point: {}\nx,y: {:.2f}, {:.2f}".format(idx, x, y))
            else:
                ann.set_text('???')

    def hide_annotations(self):
        for ann in self.annotations:
            ann.set_visible(False)
        

# ---------------------------------------------------------------------

t = np.linspace(0.0, 1.0, 11)

s1 = t
s2 = -t
s3 = t**2
s4 = -(t**2)
s5 = np.sin(t*2*np.pi)
s6 = np.cos(t*2*np.pi)

fig = figure()

ax1 = fig.add_subplot(321)
ax1.plot(t, s1)
ax1.scatter(t, s1)

ax2 = fig.add_subplot(322)
ax2.plot(t, s2)
ax2.scatter(t, s2)

ax3 = fig.add_subplot(323)
ax3.plot(t, s3)
ax3.scatter(t, s3)

ax4 = fig.add_subplot(324)
ax4.plot(t, s4)
ax4.scatter(t, s4)

ax5 = fig.add_subplot(325)
ax5.plot(t, s5)
ax5.scatter(t, s5)

ax6 = fig.add_subplot(326)
ax6.plot(t, s6)
ax6.scatter(t, s6)

multi = MyCursor(fig.canvas, (ax1, ax2, ax3, ax4, ax5, ax6))

show()
