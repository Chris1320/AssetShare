import { Card } from "@heroui/react"
import { createFileRoute } from "@tanstack/react-router"

import { DESCRIPTION, NAME, VERSION } from "@/lib/info"

export const Route = createFileRoute("/")({ component: HomePage })

export function HomePage() {
  return (
    <main className="flex min-h-screen items-center justify-center p-6">
      <Card className="w-full max-w-md">
        <Card.Header>
          <Card.Title>{NAME}</Card.Title>
          <Card.Description>{DESCRIPTION}</Card.Description>
        </Card.Header>
        <Card.Content>
          Hello from {NAME} v{VERSION}!
        </Card.Content>
      </Card>
    </main>
  )
}
