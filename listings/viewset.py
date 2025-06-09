class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        search_query = request.query_params.get("q", "")
        if not search_query:
            return Response({"error": "Search query is required"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(
            Q(bill_email__icontains=search_query)
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)