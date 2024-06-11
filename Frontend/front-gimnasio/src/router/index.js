import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/Login.vue'
import RegisterUserView from './../components/RegisterUser.vue'
import DashboardView from '@/components/Dashboard.vue'
import ProductosView from '@/components/Productos.vue'
import DetallesProductosView from '@/components/DetallesProductos.vue'
import PromocionesView from '@/components/Promociones.vue'
import DetallesPromocionesView from '@/components/DetallesPromociones.vue'
import PedidosView from '@/components/Pedidos.vue'
import DetallesPedidosView from '@/components/DetallesPedidos.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children:[
        {path: '/personas', name: 'personas', component: RegisterUserView},
        {path: '/productos', name: 'productos', component: ProductosView},
        {path: '/detallesProductos', name: 'detallesProductos', component: DetallesProductosView},
        {path: '/pedidos', name: 'pedidos', component: PedidosView},
        {path: '/detallesPedidos', name: 'detallesPedidos', component: DetallesPedidosView},
        {path: '/promociones', name: 'promociones', component: PromocionesView},
        {path: '/detallesPromociones', name: 'detallesPromociones', component: DetallesPromocionesView},
      ]
    }
  ]
})

export default router
