import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'profile',
    loadComponent: () =>
      import('./features/profile/profile.component').then(
        (mod) => mod.ProfileComponent
      ),
  },
  {
    path: 'signin',
    loadComponent: () =>
      import('./features/signin/signin.component').then(
        (mod) => mod.SigninComponent
      ),
  },
  {
    path: 'market',
    loadComponent: () =>
      import('./features/market/market.component').then(
        (mod) => mod.MarketComponent
      ),
  },
  {
    path: '',
    pathMatch: 'full',
    loadComponent: () =>
      import('./features/home/home.component').then((mod) => mod.HomeComponent),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
