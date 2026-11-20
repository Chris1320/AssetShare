import { render, screen } from "@testing-library/react"
import { describe, expect, it } from "vitest"

import { DESCRIPTION, NAME, VERSION } from "@/lib/info"
import { HomePage } from "@/routes/index"

describe("HomePage", () => {
  it("renders the application title, description, and greeting", () => {
    render(<HomePage />)

    expect(screen.getByText(NAME)).toBeDefined()
    expect(screen.getByText(DESCRIPTION)).toBeDefined()
    expect(screen.getByText(`Hello from ${NAME} v${VERSION}!`)).toBeDefined()
  })
})
