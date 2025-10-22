describe("Backend connectivity test", () => {
  it("should fetch /api/addresses successfully", () => {
    // Replace with a real endpoint in your FastAPI app
    const backendUrl = "http://localhost:8000/address";

    cy.request(backendUrl).then((response) => {
      // Expect status 200
      expect(response.status).to.eq(200);

      // Optionally, check response body has something
      expect(response.body).to.have.property("length");
      expect(response.body.length).to.be.greaterThan(0);
    });
  });
});