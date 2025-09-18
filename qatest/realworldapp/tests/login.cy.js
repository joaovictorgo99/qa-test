describe('login', () => {
    it('log in to an account', () => {
        cy.visit('http://localhost:3000/')
        cy.get('[name="username"]').type("richg")
        cy.get('[name="password"]').type("1234")
        cy.get('[data-test="signin-submit"]').click()
        cy.get('[data-test="nav-public-tab"]').contains("Everyone")
    })
})
