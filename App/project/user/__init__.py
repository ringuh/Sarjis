# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, url_for, Blueprint
from project import db
from form import LoginForm
from project.models import User
from flask.ext.login import current_user, login_required, login_user, logout_user
from sqlalchemy import func
from project.mobile.views import TeamCheck, OrgaCheck, Assistant, Member, VisitorLog
from flask.ext.babel import lazy_gettext, gettext
from project.mylog import Log