from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Informations Patients !"

    name = fields.Char(string="Nom patient", required= True)
    age = fields.Integer(string= "Age")
    is_child = fields.Boolean(string = "Est un enfant ?")
    note = fields.Text(string = "Notes")
    gens = fields.Selection([('homme', 'Homme'), ('femme', 'Femme'), ('autre', 'Autre')], string = 'Gens')