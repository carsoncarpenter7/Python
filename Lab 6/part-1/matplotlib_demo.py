#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-10-22
# carson.carpenter7@csu.fullerton.edu
#
# Examples taken from various gallery items at
# https://matplotlib.org/gallery

""" Program for manipulating Matplotlibs """

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
from time import sleep

# source env/bin/activate


def fill_between_demo():
    """ Fill Between Demo from matplotlib """
    # https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/fill_between_demo.html
    # fill_between_demo.py
    x_plot = np.arange(0.0, 2, 0.01)
    y1_plot = np.sin(2 * np.pi * x_plot)
    y2_plot = 1.2 * np.sin(4 * np.pi * x_plot)
    ###########################################################################

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

    ax1.fill_between(x_plot, 0, y1_plot)
    ax1.set_ylabel('between y1 and 0')
    fig.savefig('a.pdf')

    ax2.fill_between(x_plot, y1_plot, 1)
    ax2.set_ylabel('between y1 and 1')
    fig.savefig('b.pdf')

    ax3.fill_between(x_plot, y1_plot, y2_plot)
    ax3.set_ylabel('between y1 and y2')
    ax3.set_xlabel('x')
    fig.savefig('c.pdf')

    ###########################################################################
    # Now fill between y1 and y2 where a logical condition is met.  Note
    # this is different than calling
    # ``fill_between(x[where], y1[where], y2[where] ...)``
    # because of edge effects over multiple contiguous regions.

    fig, (axis, ax1) = plt.subplots(2, 1, sharex=True)
    axis.plot(x_plot, y1_plot, x_plot, y2_plot, color='black')
    axis.fill_between(x_plot, y1_plot, y2_plot, where=y2_plot >= y1_plot,
                      facecolor='green', interpolate=True)
    axis.fill_between(x_plot, y1_plot, y2_plot, where=y2_plot <= y1_plot,
                      facecolor='red', interpolate=True)
    axis.set_title('fill between where')

    # Test support for masked arrays.
    y2_plot = np.ma.masked_greater(y2_plot, 1.0)
    ax1.plot(x_plot, y1_plot, x_plot, y2_plot, color='black')
    ax1.fill_between(x_plot, y1_plot, y2_plot, where=y2_plot >= y1_plot,
                     facecolor='green', interpolate=True)
    ax1.fill_between(x_plot, y1_plot, y2_plot, where=y2_plot <= y1_plot,
                     facecolor='red', interpolate=True)
    ax1.set_title('Now regions with y2>1 are masked')
    ###########################################################################
    # This example illustrates a problem; because of the data
    # gridding, there are undesired unfilled triangles at the crossover
    # points.  A brute-force solution would be to interpolate all
    # arrays to a very fine grid before plotting.
    ###########################################################################
    # Use transforms to create axes spans where a
    # certain condition is satisfied:

    fig, axis = plt.subplots()
    y_axis = np.sin(4 * np.pi * x_plot)
    axis.plot(x_plot, y_axis, color='black')
    # use data coordinates for the x-axis and the axes coordinates
    # for the y_axis-axis
    import matplotlib.transforms as mtransforms
    trans = mtransforms.blended_transform_factory(axis.transData,
                                                  axis.transAxes)
    theta = 0.9
    axis.axhline(theta, color='green', lw=2, alpha=0.5)
    axis.axhline(-theta, color='red', lw=2, alpha=0.5)
    axis.fill_between(x_plot, 0, 1, where=y_axis > theta,
                      facecolor='green', alpha=0.5, transform=trans)
    axis.fill_between(x_plot, 0, 1, where=y_axis < -theta,
                      facecolor='red', alpha=0.5, transform=trans)


def simple_plot():
    """ Simple Demo from matplotlib """
    # https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
    # Data for plotting
    # Modified to write only to a file and close the figure.
    t_range = np.arange(0.0, 2.0, 0.01)
    s_range = 1 + np.sin(2 * np.pi * t_range)

    fig, axis = plt.subplots()
    axis.plot(t_range, s_range, 'C2')

    axis.set(xlabel='time (s)', ylabel='voltage (mV)',
             title='About as simple as it gets, folks')
    axis.grid()
    print('Writing out figure to simple_plot.png')
    fig.savefig("simple_plot.png")
    plt.close()


def timeline():
    """ Timeline demo from matplotlib """
    # https://matplotlib.org/gallery/lines_bars_and_markers/timeline.html#sphx-glr-gallery-lines-bars-and-markers-timeline-py
    # Modified to write only to a file and close the figure.

    names = ['v2.2.4', 'v3.0.3', 'v3.0.2', 'v3.0.1', 'v3.0.0', 'v2.2.3',
             'v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0',
             'v2.0.2', 'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1',
             'v1.5.0', 'v1.4.3', 'v1.4.2', 'v1.4.1', 'v1.4.0']

    dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
             '2014-10-26', '2014-10-18', '2014-08-26']

    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(d_obj, "%Y-%m-%d") for d_obj in dates]
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, axis = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    axis.set(title="Matplotlib release dates")

    axis.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
    axis.plot(dates, np.zeros_like(dates), "-o",
              color="k", markerfacecolor="w")  # Baseline and markers on it.

    # annotate lines
    for d_obj, l_obj, r_obj in zip(dates, levels, names):
        axis.annotate(r_obj, xy=(d_obj, l_obj),
                      xytext=(-3, np.sign(l_obj)*3),
                      textcoords="offset points", horizontalalignment="right",
                      verticalalignment="bottom" if l_obj > 0 else "top")

    # format xaxis with 4 month intervals
    axis.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
    axis.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(axis.get_xticklabels(), rotation=30, ha="right")

    # remove y_axis axis and spines
    axis.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        axis.spines[spine].set_visible(False)

    axis.margins(y=0.1)
    print('Writing out figure to timeline.png')
    fig.savefig("timeline.png")
    plt.close()


def line_demo_dash_control():
    """Line Demo Dash control from matplotlib """
    # https://matplotlib.org/gallery/lines_bars_and_markers/line_demo_dash_control.html#sphx-glr-gallery-lines-bars-and-markers-line-demo-dash-control-py
    # Modified to write only to a file and close the figure.

    """
    ==============================
    Customizing dashed line styles
    ==============================

    The dashing of a line is controlled via a dash sequence. It can be modified
    using `.Line2D.set_dashes`.

    The dash sequence is a series of on/off lengths in points, e.g.
    ``[3, 1]`` would be 3pt long lines separated by 1pt spaces.

    Some functions like `.Axes.plot` support passing Line properties as keyword
    arguments. In such a case, you can already set the dashing when
    creating the line.

    *Note*: The dash style can also be configured via a
    :doc:`property_cycle </tutorials/intermediate/color_cycle>`
    by passing a list of dash sequences using the keyword *dashes* to the
    cycler. This is not shown within this example.
    """
    # import numpy as np
    # import matplotlib.pyplot as plt

    x_plot = np.linspace(0, 10, 500)
    y_axis = np.sin(x_plot)

    fig, axis = plt.subplots()

    # Using set_dashes() to modify dashing of an existing line
    line1, = axis.plot(x_plot, y_axis, label='Using set_dashes()')
    line1.set_dashes([2, 2, 10, 2])
    # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    line2, = axis.plot(x_plot, y_axis - 0.2, dashes=[6, 2],
                       label='Using the dashes parameter')
    line2.set_dashes([3, 5, 1, 5])

    axis.legend()
    # save the file
    print('Writing out figure to line_demo_dash_control.png')
    fig.savefig("line_demo_dash_control.png")
    plt.close()
    plt.show()


def main():
    """ Calling functions to create graphs """
    simple_plot()
    line_demo_dash_control()
    timeline()
    fill_between_demo()


if __name__ == "__main__":
    main()
