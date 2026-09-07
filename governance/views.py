from django.db.models.aggregates import Avg
from django.shortcuts import get_object_or_404, render
from governance.models import Aspect, ElementAssessment

# Create your views here.
def governance_overview(request):
    # All element assessments currently in the system
    element_assessments = ElementAssessment.objects.all()

    # Overall current maturity
    overall_maturity = (
        element_assessments
        .filter(maturity__isnull=False)
        .aggregate(avg=Avg("maturity__value"))["avg"]
    )

    # Coverage:
    # percentage of governance elements that have an assessment
    total_elements = Aspect.objects.filter(
        elements__active=True
    ).values("elements").distinct().count()

    assessed_elements = (
        element_assessments
        .values("element")
        .distinct()
        .count()
    )

    coverage = (
        (assessed_elements / total_elements) * 100
        if total_elements
        else 0
    )

    # Maturity by governance aspect
    aspects = []

    for aspect in Aspect.objects.all():
        assessments = element_assessments.filter(
            element__aspect=aspect,
            maturity__isnull=False,
        )

        maturity = assessments.aggregate(
            avg=Avg("maturity__value")
        )["avg"]

        aspects.append({
            "name": aspect.name,
            "maturity": maturity,
            "order": aspect.order
        })

    context = {
        "overall_maturity": overall_maturity,
        "coverage": coverage,
        "aspects": aspects,
    }

    return render(
        request,
        "index.html",
        context,
    )


def aspect_detail(request, aspect_order):
    aspect = get_object_or_404(
        Aspect,
        order=aspect_order
    )

    elements = aspect.elements.filter(
        active=True
    )

    element_data = []

    for element in elements:

        assessment = (
            ElementAssessment.objects
            .filter(element=element)
            .order_by("-id")
            .first()
        )

        element_data.append({
            "element": element,
            "assessment": assessment,
        })

    context = {
        "aspect": aspect,
        "elements": element_data,
    }

    return render(
        request,
        "aspect_detail.html",
        context,
    )