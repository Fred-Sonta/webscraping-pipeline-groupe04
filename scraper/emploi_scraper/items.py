import scrapy

class EntrepriseItem(scrapy.Item):
    """Modèle pour les données de l'entreprise (Axe Profils des Entreprises)"""
    nom_entreprise = scrapy.Field()
    secteur_activite = scrapy.Field()
    site_web = scrapy.Field()
    description_employeur = scrapy.Field()

class OffreItem(scrapy.Item):
    """Modèle pour les données de l'offre d'emploi (Axe Dynamique de l'Emploi)"""
    id_emploi_ci = scrapy.Field()  # Identifiant unique sur le site
    titre_poste = scrapy.Field()
    nom_entreprise = scrapy.Field() # Clé de liaison temporaire
    categorie_portail = scrapy.Field() # 'IT', 'Freelance', 'Standard'
    
    # Géographie et Modalités
    ville = scrapy.Field()
    type_contrat = scrapy.Field()
    
    # Critères
    niveau_etude_requis = scrapy.Field()
    experience_requise = scrapy.Field()
    
    # Dates
    date_publication = scrapy.Field()
    date_limite = scrapy.Field()
    
    # Textes bruts pour NLP
    description_mission = scrapy.Field()
    profil_recherche = scrapy.Field()

    