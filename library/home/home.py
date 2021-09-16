from flask import Blueprint, render_template, redirect, url_for, session, request

import library.adapters.repository as repo

import library.utilities.utilities as utilities

# configure blueprint
home_blueprint = Blueprint(
    "home_bp", __name__, url_prefix="/")


@home_blueprint.route('/')
def home():

    form = utilities.SearchForm()

    return render_template(
        "home/home.html",
        form=form
    )
