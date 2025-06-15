import { Outlet, createRootRoute } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'

export const Route = createRootRoute({
  component: () => (
    <div className="bg-[#232323] text-white min-h-screen flex flex-col">
      <Outlet />
      <TanStackRouterDevtools />
    </div>
  ),
})
