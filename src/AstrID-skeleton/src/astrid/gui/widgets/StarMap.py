import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import AltAz, SkyCoord, solar_system_ephemeris
from astropy.time import Time
from matplotlib.patches import Circle
from sparrow.conf.telescope import GBT
from sparrow.data.LoadCatalog import LoadHipparcos

# Set the ephemeris
solar_system_ephemeris.set("jpl")


def stars_in_alt_az(alt_az, observing_time, magnitude_limit=10):
    # Load the Hipparcos catalog
    stars_all = LoadHipparcos()
    # Clip to magnitude limit
    stars = stars_all[stars_all.magnitude <= magnitude_limit]
    # milliarcsec/year units
    mas_yr = 1e-6 * u.arcsec / u.year
    coords = SkyCoord(
        frame="icrs",
        ra=stars["ra_degrees"].values * u.degree,
        dec=stars["dec_degrees"].values * u.degree,
        pm_ra_cosdec=stars["ra_mas_per_year"].values * mas_yr,
        pm_dec=stars["dec_mas_per_year"].values * mas_yr,
        obstime=observing_time,
    )
    coords.transform_to(alt_az)
    coords.representation_type = "cartesian"
    stars["x"] = coords.x
    stars["y"] = coords.y
    return stars


def magnitude_to_marker_size(magnitudes, max_star_size=100):
    """Turn star magnitudes into plot marker sizes"""
    marker_sizes = max_star_size * 10 ** (np.divide(magnitudes, -2.5))
    return marker_sizes


def plot_stars(observing_location, observing_time):
    """Plot the stars at a given time"""

    telescope_alt_az = AltAz(location=observing_location, obstime=observing_time)
    stars = stars_in_alt_az(telescope_alt_az, observing_time)

    fig, ax = plt.subplots()

    border = plt.Circle((0, 0), 1, color="navy", fill=True)
    ax.add_patch(border)

    print(stars["magnitude"])
    marker_sizes = magnitude_to_marker_size(stars["magnitude"].values)

    ax.scatter(
        stars.x.values,
        stars.y.values,
        s=marker_sizes,
        color="white",
        marker=".",
        linewidths=0,
        zorder=2,
    )

    horizon = Circle((0, 0), radius=1, transform=ax.transData)
    for col in ax.collections:
        col.set_clip_path(horizon)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    plt.axis("off")
    plt.show()


# Load the telescope
telescope = GBT()
observing_location = telescope.EarthLocation
lat = telescope.latitude
long = telescope.longitude
observing_time = Time("2024-09-22 23:22")

plot_stars(observing_location, observing_time)
