def get_local_culture_tips(destination: str) -> dict:
    """Return local culture tips for a destination.

    Provides typical dishes, important local customs and useful phrases
    so the traveler can connect better with the local culture.

    Args:
        destination: Travel destination.

    Returns:
        Dictionary with typical dishes, customs and useful phrases.
    """
    destination_normalized = destination.lower().strip()

    culture_db = {
        "cusco": {
            "dishes": ["Cuy al horno", "Chiri uchu", "Lechón cusqueño"],
            "customs": [
                "Pedir permiso antes de fotografiar a personas locales.",
                "Respetar los rituales de pago a la tierra (pachamama).",
            ],
            "phrases": ["Allillanchu (¿Cómo estás? en quechua)", "Sulpayki (Gracias en quechua)"],
        },
        "arequipa": {
            "dishes": ["Rocoto relleno", "Chupe de camarones", "Adobo arequipeño"],
            "customs": [
                "El almuerzo de los domingos en picantería es una tradición familiar.",
                "Orgullo regional muy marcado: valora la identidad arequipeña.",
            ],
            "phrases": ["¡Qué rico el rocoto!", "¿Dónde queda la picantería?"],
        },
        "buenos aires": {
            "dishes": ["Asado", "Empanadas", "Milanesa"],
            "customs": [
                "Compartir el mate es señal de amistad.",
                "La cena suele ser tarde, después de las 21:00.",
            ],
            "phrases": ["¿Todo bien, che?", "¿Me pasás el mate?"],
        },
        "paris": {
            "dishes": ["Croissant", "Baguette", "Ratatouille"],
            "customs": [
                "Saludar con 'Bonjour' al entrar a una tienda es esperado.",
                "Las propinas no son obligatorias pero se agradecen.",
            ],
            "phrases": ["Bonjour (Buenos días)", "Merci (Gracias)", "S'il vous plaît (Por favor)"],
        },
    }

    tips = culture_db.get(destination_normalized)

    if tips is None:
        return {
            "status": "not_found",
            "destination": destination,
            "message": (
                "No hay datos culturales precargados para este destino. "
                "Investiga platos típicos, costumbres locales y frases útiles antes de viajar."
            ),
        }

    return {
        "status": "success",
        "destination": destination,
        "typical_dishes": tips["dishes"],
        "local_customs": tips["customs"],
        "useful_phrases": tips["phrases"],
    }
